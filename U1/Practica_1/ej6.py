"""Ejercicio 6. Escribir un programa, llamado rot13.py que reciba un archivo de texto de origen
y uno de destino, de modo que para cada línea del archivo origen, se guarde una línea
cifrada en el archivo destino. El algoritmo de cifrado a utilizar será muy sencillo: a cada
carácter comprendido entre la a y la z, se le suma 13 y luego se aplica el módulo 26, para
obtener un nuevo carácter."""

from string import ascii_letters, ascii_lowercase, ascii_uppercase

def rot13(fichero_origen, fichero_destino):

    letra_encrypt = ""

    for linea in fichero_origen:

        for letra in linea:
            if ascii_letters.__contains__(letra):
                
                if letra != " " and letra and letra  != "\n": 
                #saber si es mayuscula o minuscula
                    if letra.islower(): #si la letra es minuscula
                        #guardarme el numero de la letra +13 % 26 (abecedario)
                        letra_encrypt = (ascii_lowercase.index(letra) + 13) % 26
                        fichero_destino.write(ascii_lowercase[letra_encrypt])

                    else:
                        letra_encrypt = (ascii_uppercase.index(letra) + 13) % 26
                        fichero_destino.write(ascii_uppercase[letra_encrypt])
                
                else:
                    fichero_destino.write(" ")

            else:
                fichero_destino.write(letra)

def decrypt(fichero_origen, fichero_destino):

    letra_encrypt = ""

    for linea in fichero_origen:

        for letra in linea:
            if ascii_letters.__contains__(letra):
                
                if letra != " " and letra and letra  != "\n": 
                #saber si es mayuscula o minuscula
                    if letra.islower(): #si la letra es minuscula
                        #guardarme el numero de la letra +13 % 26 (abecedario)
                        letra_encrypt = (ascii_lowercase.index(letra) - 13) % 26
                        fichero_destino.write(ascii_lowercase[letra_encrypt])

                    else:
                        letra_encrypt = (ascii_uppercase.index(letra) - 13) % 26
                        fichero_destino.write(ascii_uppercase[letra_encrypt])
                
                else:
                    fichero_destino.write(" ")

            else:
                fichero_destino.write(letra)

nombre_fichero = "fundacion.txt"

#encruiptar
destino = open("encrypted_fundación.txt", "w", encoding="utf8")
archivo = open(nombre_fichero, encoding="utf8")
rot13(archivo, destino)
archivo.close()
destino.close()
#desencriptar
to_decrypt = open("encrypted_fundación.txt", encoding="utf8")
to_decrypt_result = open("decrypt13.txt", "w", encoding="utf8")
decrypt(to_decrypt, to_decrypt_result)
to_decrypt.close()