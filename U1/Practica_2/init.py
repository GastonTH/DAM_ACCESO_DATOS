from objs import Agenda, Contacto

def menu():
    print("Bienvenido a la agenda, que desea hacer "+
        "1. Guardar los datos de un contacto\n" +
        "2. Modificar datos de un contacto\n" +
        "3. Dar de baja a un contacto\n" +
        "4. Buscar un contacto\n" +
        "5. Mostrar la lista de contactos ordenada\n" +
        "6. Salir de la agenda")

ctn1 = Contacto()

ctn1.nombre = "Pepe"
ctn1.apellido1 = "Rosario"
ctn1.apellido2 = "Antunez"
ctn1.email = "aaa@aaa.aaa"
ctn1.telefono1 = str(123456789)
ctn1.telefono2 = str(987654321)
ctn1.direccion = "Calle de las piruletas"

print(ctn1.toString)
