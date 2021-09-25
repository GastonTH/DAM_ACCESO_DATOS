"""Ejercicio 3. Escribir un programa, llamado cut.py, que dado un archivo de texto, un
delimitador, y una lista de campos, imprima solamente esos campos, separados por ese
delimitador"""

import csv

"""La funcion a la que le pasas el fichero ya abierto, el delimitador de este y los campos a mostrar, muestra por pantalla el resultado 
de este"""
def cut(fichero_csv, delimitador, campos):

    archivo_csv = csv.reader(fichero_csv, delimiter=delimitador)
    contador = 0
    campos_pasar = []
    identidicadores = {"provincia":0, "poblacion":1, "codigopostalid":2, "lat":3, "lon":4}
    
    for to_add in campos:
        print(to_add,"campo")
        campos_pasar.append(identidicadores.get(to_add))

    for linea in archivo_csv:
        for campo_csv in campos_pasar:
            print(linea[campo_csv], end=" ")
        contador+=1
        print(" ")

nombre_fichero = "listado-codigos-postales.csv"
archivo = open(nombre_fichero, "r", encoding="utf8")

cut(archivo, ";", ["poblacion", "codigopostalid"])

archivo.close()