"""Ejercicio 4. Escribir un programa, llamado wc.py que reciba un archivo, lo procese e
imprima por pantalla cuántas líneas, cuantas palabras y cuántos caracteres contiene el
archivo.
"""

def wc(fichero):

    suma_caracteres = 0
    numero_lineas = 0
    numero_palabras = 0

    for linea in fichero:
        if linea != " ":
            suma_caracteres+= len(linea)
            numero_lineas+=1
            numero_palabras += len(linea.split())

    print("Hay {0} caracteres, {1} de palabras y {2} de lineas".format(suma_caracteres, numero_palabras, numero_lineas))        


nombre_fichero = "fundacion.txt"
archivo = open(nombre_fichero, encoding="utf8")

wc(archivo)

archivo.close()
