# -*- coding: utf-8 -*-

from gi.repository import Nautilus, GObject
import os
import urllib
import subprocess

TERMINAL = 'comando'


def uriPath(nautilus_file):
    ##
    # Convierte nautilus-file-uri en una ruta válida si es posible '
    #
    if nautilus_file.get_uri_scheme() == 'file':
        return urllib.unquote(nautilus_file.get_uri()[7:])
    elif 'x-nautilus-desktop' in nautilus_file.get_uri_scheme():
        ## Para analizar los posibles directorios de trabajo de los usuarios

        directorios = ['~/Desktop', '~/Escritorio', '~/Workspace', '~/']
        for directorio in directorios:
            escritorio = os.path.expanduser(directorio)
            if os.path.exists(escritorio):
                return escritorio


def getTerminal():
    return TERMINAL


def runTerminal(path):
    # Se cambia al directorio actual de trabajo
    # y se llama al terminal elegido
    os.chdir(path)
    subprocess.call([getTerminal()])


##
# Añade la nueva entrada al menú
# contextual de nautilus
class ColumnExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

    def menu_activate_cb(self, menu, nautilus_file):
        runTerminal(uriPath(nautilus_file))

    def get_file_items(self, window, nautilus_files):
        if nautilus_files != [] and os.path.isdir(uriPath(nautilus_files[0])):
            item = Nautilus.MenuItem(
                name='TerminalExtension::Open terminal here',
                label='string',
                tip='string'
            )
            item.connect('activate', self.menu_activate_cb, nautilus_files[0])

            return item,

    def get_background_items(self, window, nautilus_file):
        item = Nautilus.MenuItem(
            name='TerminalExtension::Open terminal here',
            label='string',
            tip='string'
        )
        item.connect('activate', self.menu_activate_cb, nautilus_file)

        return item,
