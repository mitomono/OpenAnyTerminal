#! /usr/bin/python

from os import makedirs
from shutil import copy
from getpass import getuser
import gettext
import errno

gettext.textdomain("install")
gettext.bindtextdomain("install", "./mo")

# Read de command for launch the terminal
command_term = raw_input(gettext.gettext('Enter the command you want to open in the menu: '))

user = getuser()
orig = './OpenAnyTerminal.py'
# dest = '/home/'+user+'/.local/share/nautilus-python/extensions/Open_'+command_term+'_Terminal.py'
path = '/home/' + user + '/.local/share/nautilus-python/extensions'
dest = path + '/' + 'Open_' + command_term + '_Terminal.py'


def make_sure_path_exists(pth):
    try:
        makedirs(pth)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def install():
    copy(orig, dest)

    # Open file extension
    f = open(orig)

    # Read full file, save the text and replace the string "comando" by command_term
    prog = command_term.split('-', 1)

    texto = f.read()
    texto = texto.replace('comando', command_term)
    texto = texto.replace('Programa', prog[0])
    texto = texto.replace('string', gettext.gettext('Open ') + command_term + gettext.gettext(' here'))

    # Close file
    f.close()

    # Reopen the file and writes the changed text
    salida = open(dest, 'w')
    salida.write(texto)
    salida.close()


make_sure_path_exists(path)
install()
