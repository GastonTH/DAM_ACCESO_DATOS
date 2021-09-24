"""Ejercicio 2. Escribir un programa, llamado cp.py, que copie todo el contenido de un archivo
a otro, de modo que quede exactamente igual.
"""

def cp(fichero, original):
    nuevo_fichero = open("Copy_" + original, "w")

    for linea in fichero:
        nuevo_fichero.write(linea)

    nuevo_fichero.close()

nombre_fichero_a_copiar = "fundacion.txt"
fichero_a_copiar = open(nombre_fichero_a_copiar)

cp(fichero_a_copiar, nombre_fichero_a_copiar)

fichero_a_copiar.close()