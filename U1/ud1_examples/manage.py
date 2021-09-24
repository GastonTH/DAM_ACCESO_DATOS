archivo = open("archivo.txt")

# tres formas

linea=archivo.readline()
while linea != '':
    # procesar línea
    línea=archivo.readline()
    print(linea)

for linea in archivo:
    # procesar línea
    print(linea)

lineas = archivo.readlines()
for línea in lineas:
    # procesar línea
    print(linea)

# liberar memoria siempre
# ficheros pequeños tienen un pequeño impacto
# con ficheros grandes cuidado con la memoria
archivo.close()
