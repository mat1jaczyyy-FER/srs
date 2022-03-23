#!/usr/bin/env python3
# Dominik Matijaca 0036524568

from sys import argv, exit

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

def error(x):
    print(x)
    exit(1)

data = {}

def save():
    as_list = [i.encode('utf-8') for i in list(data.keys()) + list(data.values())]
    bytes = b'\0'.join(as_list)

    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(bytes)
    
    with open("data.bin", "wb") as f:
        f.write(cipher.nonce)
        f.write(tag)
        f.write(ciphertext)

def load():
    try:
        with open("data.bin", "rb") as f:
            nonce = f.read(16)
            tag = f.read(16)
            ciphertext = f.read()

    except FileNotFoundError:
        error("Password manager not initialized.")

    cipher = AES.new(key, AES.MODE_EAX, nonce)

    try:
        bytes = cipher.decrypt_and_verify(ciphertext, tag)
    
    except ValueError:
        error("Master password incorrect or integrity check failed.")

    as_list = [i.decode('utf-8') for i in bytes.split(b'\0')]

    cnt = len(as_list) // 2
    for i in range(cnt):
        data[as_list[i]] = as_list[i + cnt]

def tajnik_action_init(arg):
    save()
    print("Password manager initialized.")

def tajnik_action_get(arg):
    load()

    try:
        site = arg[0]

    except IndexError:
        error("No site specified.")
    
    try:
        pw = data[site]

    except KeyError:
        error(f"There is no password stored for {site}.")
    
    print(f"Password for {site} is: {pw}")

def tajnik_action_put(arg):
    load()

    try:
        site = arg[0]

    except IndexError:
        error("No site specified.")
    
    try:
        pw = arg[1]

    except IndexError:
        error("No password specified.")
    
    data[site] = pw
    save()

    print(f"Stored password for {site}.")

try:
    action = globals()[f"tajnik_action_{argv[1]}"]

except KeyError:
    error("Unknown action.")

except IndexError:
    error("No action specified.")

try:
    key = argv[2]

except IndexError:
    error("No master password specified.")

key = PBKDF2(key, "fer-srs", dkLen = 32)
action(argv[3:])
