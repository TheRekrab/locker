# The Locker Project
The Locker project is my attempt at creating a piece of safe, open source, and free data encryption software. That's just me saying that I was kind of interested in learning more about Cryptography and the Python `cryptography` library.

## Installation
The project is pretty simple.

1. Download the repository:
```bash
$ git clone https://github.com/TheRekrab/locker
```

2. Ensure that the file has executable permissions:
```bash
$ chmod +x locker.py
```

3. Copy the file onto PATH:
```bash
$ sudo cp locker.py /usr/local/bin/locker
```

You can now run the command `locker` from the terminal, and you will have full access to the app from anywhere in your computer.

## How to use it:
After being installed, you can simply run `locker` in the terminal to see the options.
```
$ locker
Usage: locker [MODE] [FILEPATH(s)]

Options:
	-e / --encrypt		Encryption mode, encrypt files
	-d / --decrypt		Decryption mode, decrypt files


```

To **encrypt** a file:
```bash
$ locker -e myfile.txt myotherfile.txt
```
You will be prompted for a password:
```
Please enter the password you would like to use during this operation: 
```
Choose a password that you will remember. Your file will be encrypted by `locker` and will appear to be gibberish to anybody that tries to see it.

To **decrypt** a file:
```bash
$ locker -d myfile.txt myotherfile.txt
```
Again, you will be prompted with a password:
```
Please enter the password you would like to use during this operation: 
```
It is incredibly important that you remember your password! If you forget it, all of your data is **LOST FOREVER**!!!

If you enter the correct password, your files will quickly and silently be decrypted. You will have full access to the file. You can then re-encrypt it with any password you choose.

## Examples:
With this project, I have included a directory called `examples`. Once you have installed `locker`, `cd` into that directory. There are 2 files, `encryptme.txt`, and `decryptme.txt`. The password to decrypt `decryptme.txt` is `locker`.

---

I hope you enjoy using `locker`.