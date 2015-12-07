# README

Inspirado en la extensión open-terminal de nautilus.

Con esta extensión obtenemos la funcionalidad de abrir nuestro terminal de comandos preferido, pudiendo ser cualquiera, en el directorio en el que deseemos solo con pulsar con el botón derecho del ratón en un directorio y seleccionar la opción. ya que con la extension original de nautilus solo nos abre el terminal por defecto de gnome, gnome-terminal, asi damos opcion a usar otros.

-----
### Requisitos:
Es necesario instalar **Python** en nuestra distribución y el paquete **nautilus-python**:

#####Ubuntu
1. para instalar python:
	* ` sudo apt-get install  python `
2. para instalar nautilus-python:
	* `sudo apt-get install nautilus.python`

#####fedora
* fedora >=22
1. para instalar python:
	* ` sudo dnf install  python `
2. para instalar nautilus-python:
	* `sudo dnf install nautilus.python`

* fedora <22
1. para instalar python:
	* ` sudo yum install  python `
2. para instalar nautilus-python:
	* `sudo yum install nautilus-python`

* En general
	instalar python y nautilus-python con su gestor de paquetes

------
### INSTALACIÓN
Descargar los archivos, situarse en la carpeta donde se se encuentran
y darles permisos de ejecución:

   ` chmod +x ./* `

a continuacion:

` python install.py `

o

` ./install.py `

   se le preguntara que cual es el comando para abrir el terminal que desee, escriba el comando que lance el terminal elegido y pulse intro.

algunos ejemplos de comandos para ejecutar terminales:
* `gnome-terminal` *terminal por defecto de gnome*
* `terminator`
* `xterminal`
* `terminology`
* `finalterm`
* `byobu`

etc

Previamente se debera de tener instalado uno de estos terminales

una vez instalado reiniciar nautilus con:

` nautilus -q`

o reiniciando la sesion o el ordenador, si se queda bloqueado.Una vez reiniciado
la extension apararecera en el menu del boton secundario de nautilus.

disfrute.

------
### DESINSTALACIÓN
En la carpeta donde se descargaron los archivos:

   ` ./uninstall `
