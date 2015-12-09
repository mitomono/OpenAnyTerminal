#! /usr/bin/python

import os, getpass

user = getpass.getuser()

os.remove('/home/'+user+'/.local/share/nautilus-python/extensions/OpenAnyTerminal.pyc')
os.remove('/home/'+user+'/.local/share/nautilus-python/extensions/OpenAnyTerminal.py')
