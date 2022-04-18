#!/usr/bin/env python3
# Dominik Matijaca 0036524568

from sys import argv, byteorder, exit
from getpass import getpass

from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes

def error(x):
    print(x)
    exit(1)

data = {}

def save():
    with open("data.bin", "wb") as f:
        for k, v in data.items():
            f.write(len(k).to_bytes(4, byteorder))
            f.write(k.encode('utf-8'))
            for i in v:
                f.write(i)

def load():
    try:
        with open("data.bin", "rb") as f:
            while len_k := int.from_bytes(f.read(4), byteorder):
                k = f.read(len_k).decode('utf-8')
                v = [f.read(i) for i in [16, 16, 1]]
                data[k] = v

    except FileNotFoundError:
        save()

def tokey(password, salt):
    return scrypt(password, salt, 16, N=2**15, r=8, p=1)

def set(username, password):
    salt = get_random_bytes(16)
    key = tokey(password, salt)

    data[username] = [salt, key, b'\x00']

def getpass_test(prompt):
    try:
        password = input(prompt)
    except EOFError:
        exit(0)
        
    print(password)
    return password

getpass_impl = getpass_test if "--test" in argv else getpass

def getpass_repeat(prompt, error_msg):
    password = getpass_impl(f"{prompt}: ")
    
    if len(password) < 10:
        error(f"{error_msg}. Password should be at least 10 characters.")

    repeat = getpass_impl(f"Repeat {prompt}: ")

    if password != repeat:
        error(f"{error_msg}. Password mismatch.")
    
    return password
