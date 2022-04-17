#!/usr/bin/env python3
# Dominik Matijaca 0036524568

from common import *

def usermgmt_action_add():
    load()

    if username in data:
        error("User add failed. User already exists.")

    password = getpass_repeat("Password", "User add failed")

    set(username, password)
    save()

    print("User successfully added.")

def usermgmt_action_passwd():
    load()

    if username not in data:
        error("Password change failed. User does not exist.")

    password = getpass_repeat("Password", "Password change failed")

    set(username, password)
    save()

    print("Password change successful.")

def usermgmt_action_forcepass():
    load()

    if username not in data:
        error("Request to change password failed. User does not exist.")

    data[username][2] = b'\x01'
    save()

    print("User will be requested to change password on next login.")

def usermgmt_action_del():
    load()

    if username not in data:
        error("User delete failed. User does not exist.")

    del data[username]
    save()

    print("User successfully deleted.")

try:
    action = globals()[f"usermgmt_action_{argv[1]}"]

except KeyError:
    error("Unknown action.")

except IndexError:
    error("No action specified.")

try:
    username = argv[2]

except IndexError:
    error("No user specified.")

action()
