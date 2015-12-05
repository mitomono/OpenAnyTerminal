#! /usr/bin/python

# Read de command for launch the terminal
command_term = raw_input('introduce el comando para abrir el terminal deseado: ')

# Open file extension
f = open("./open-any-terminal.py", 'r')

# Read full file, save the text and replace the string "comando" by command_term
texto = f.read()
texto = texto.replace("comando", command_term)

# Close file
f.close()

# Reopen the file and writes the changed text
salida = open("./open-any-terminal.py", 'w')
salida.write(texto)
salida.close()
