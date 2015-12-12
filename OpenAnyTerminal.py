# -*- coding: utf-8 -*-

from gi.repository import Nautilus, GObject
import os
import urllib
import subprocess

TERMINAL = 'comando'
##
# algunas cadenas para editores de texto que admiten un directorio
# como parametro
CADENAS = ['sublime', 'sub', 'code', 'VS', 'atom']


def uri_path(nautilus_file):
    ##
    # Convierte nautilus-file-uri en una ruta válida si es posible '
    #
    if nautilus_file.get_uri_scheme() == 'file':
        return urllib.unquote(nautilus_file.get_uri()[7:])
    elif 'x-nautilus-desktop' in nautilus_file.get_uri_scheme():
        # Para analizar los posibles directorios de trabajo de los usuarios

        directorios = ['~/Desktop', '~/Escritorio', '~/Workspace', '~/']
        for directorio in directorios:
            escritorio = os.path.expanduser(directorio)
            if os.path.exists(escritorio):
                return escritorio


def get_terminal():
    return TERMINAL


def run_terminal(path):
    # Se cambia al directorio actual de trabajo
    # y se llama al terminal elegido
    editor = False
    for cmd in CADENAS:
        if TERMINAL.find(cmd) != -1:
            editor = True
            break

    if editor:
        os.chdir(path)
        subprocess.call([get_terminal(), path])
    else:
        os.chdir(path)
        subprocess.call([get_terminal()])


##
# Añade la nueva entrada al menú
# contextual de nautilus
class ColumnExtension_Programa(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

    def menu_activate_cb(self, menu, nautilus_file):
        run_terminal(uri_path(nautilus_file))

    def get_file_items(self, window, nautilus_files):
        if nautilus_files != [] and os.path.isdir(uri_path(nautilus_files[0])):
            item = Nautilus.MenuItem(
                    name='ColumnExtension_comando::Open comando here',
                    label='string',
                    tip='string'
            )
            item.connect('activate', self.menu_activate_cb, nautilus_files[0])

            return item,

    def get_background_items(self, window, nautilus_file):
        item = Nautilus.MenuItem(
                name='ColumnExtension_comando::Open comando here',
                label='string',
                tip='string'
        )
        item.connect('activate', self.menu_activate_cb, nautilus_file)

        return item,
