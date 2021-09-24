"""Ejercicio 1. Escribir un programa, llamado head que reciba un archivo y un número N e
imprima las primeras N líneas del archivo.
"""

def head(fichero, numero_lineas):

    for i, linea in enumerate(fichero):

        if i < numero_lineas:
            print(i,";", linea)            

to_read = open("pruebas.txt")
numero = 4

head(to_read, numero)

to_read.close()
