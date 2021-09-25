"""Ejercicio 5. Escribir un programa, llamado grep.py que reciba una expresión y un archivo e
imprima las líneas del archivo que contienen la expresión recibida."""

def grep(fichero, buscar):

    for linea in fichero:
        if buscar in linea:
            print("------- la palabra {0} esta en la linea: {1} -------".format(buscar, linea))


nombre_fichero = "fundacion.txt"
archivo = open(nombre_fichero, encoding="utf8")
palabra_buscar = "La serie de 'Fundación' es un hito de la ciencia-ficción televisiva: 7 aciertos que convierten la adaptación de Asimov en un éxito"

grep(archivo, palabra_buscar)

archivo.close()
