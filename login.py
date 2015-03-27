#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A shared module for logging a user into the github3.py api
"""
from github3 import login
from getpass import getpass, getuser
import sys

def auth():
    try:
        user = raw_input('GitHub username: ')
    except KeyboardInterrupt:
        user = getuser()

    password = getpass('GitHub password for {0}: '.format(user))

    # Obviously you could also prompt for an OAuth token
    if not (user and password):
        print("Cowardly refusing to login without a username and password.")
        sys.exit(1)

    g = login(user, password)

    return g
