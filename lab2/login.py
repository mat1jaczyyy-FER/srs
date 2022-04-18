#!/usr/bin/env python3
# Dominik Matijaca 0036524568

from common import *

try:
    username = argv[1]

except IndexError:
    error("No user specified.")

load()

while True:
    password = getpass_impl("Password: ")

    if username in data:
        key = tokey(password, data[username][0])
        
        if key == data[username][1]:
            break

    print("Username or password incorrect.")

if data[username][2] == b'\x01':
    print("Password change was requested.")

    while True:
        new_password = getpass_repeat("New Password", "Password change failed")

        if password != new_password:
            break
    
        print("Passwords must be different.")

    set(username, new_password)
    save()
    
    print("Password change successful.")

print("Login successful.")
