#! /usr/bin/python

import shutil, os, getpass
import gettext

user = getpass.getuser()
orig = './OpenAnyTerminal.py'
dest = '/home/'+user+'/.local/share/nautilus-python/extensions/OpenAnyTerminal.py'

# Read de command for launch the terminal
command_term = raw_input('introduce el comando para abrir el terminal deseado: ')

shutil.copy(orig, dest)

# Open file extension
f = open(orig, 'r')

# Read full file, save the text and replace the string "comando" by command_term
gettext.textdomain("install")
gettext.bindtextdomain("install", "./mo")

texto = f.read()
texto = texto.replace("comando", command_term)
texto = texto.replace("string", gettext.gettext('Open ' + command_term +' here'))

# Close file
f.close()

# Reopen the file and writes the changed text
salida = open(dest, 'w')
salida.write(texto)
salida.close()
