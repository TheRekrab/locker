#!/usr/bin/env python3
import base64
from sys import argv
import os
from cryptography.fernet import Fernet, InvalidToken
from getpass import getpass

def to_key(original_key):
    # Takes any string and converts it into a valid Fernet key.
    KEY_LEN = 32
    key = b""
    while len(key) < KEY_LEN:
        key += original_key.encode("utf-8")
    
    key = key[:KEY_LEN]
    b64 = base64.urlsafe_b64encode(key)
    return KEY_LEN, b64
    
def do_thing(fp, key, mode='e'):

    assert mode == 'e' or mode == 'd'

    # I would check if the file exists with an assert statement, but that's not debugging, it's more like a basic warning.
    if not os.path.exists(fp):
        print("ERROR: File \"%s\" does not exist." % fp)
        return -1
    elif os.path.isdir(fp):
        for file_path in os.scandir(fp):
            do_thing(file_path, key, mode)
        return 0

    try:
        with open(fp, "rb") as datafile:
            data = datafile.read()
    except PermissionError:
        print("ERROR: File \"%s\" could not be opened for reading, Permission Denied." % fp)
        return -1
    
    f = Fernet(key)

    if (mode == 'e'):
        new_data = f.encrypt(data)
    else:
        try:
            new_data = f.decrypt(data)
        except InvalidToken:
            print("ERROR: Incorrect password for file \"%s\"" % fp)
            return -1


    try:
        with open(fp, "wb") as newfile:
            newfile.write(new_data)
    
    except PermissionError:
        print("ERROR: File \"%s\" could not be opened for writing, Permission Denied." % fp)
        return -1
        
    return 0 # 0 means success, -1 means failure.

def display_help():
    print("Usage: %s [MODE] [FILEPATH(s)]" % os.path.basename(argv[0]))
    print("\nOptions:")
    print("\t-e / --encrypt\t\tEncryption mode, encrypt files")
    print("\t-d / --decrypt\t\tDecryption mode, decrypt files")
    print("")
    

def main():
    if len(argv) <= 2:
        display_help()
        return -1

    mode = argv[1]

    if mode == "-e" or mode == "--encrypt":
        mode = "e"
    elif mode == "-d" or mode == "--decrypt":
        mode = "d"
    else:
        print("Unknown option '%s'.\n" % argv[1])
        display_help()
        return -1

    user_key = getpass("Please enter the password you would like to use during this operation:  ").strip()
    keylen, key = to_key(user_key)
    
    assert key != None and keylen == 32

    for fp in argv[2:]:
       do_thing(fp, key, mode)

if __name__ == "__main__":
    main()
