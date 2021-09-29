class Contacto():

    DELIMITADOR = str(";")

    def __init__(self): #Constructor
        self.nombre = ""
        self.apellido1 = ""
        self.apellido2 = ""
        self.email = ""
        self.telefono1 = ""
        self.telefono2 = ""
        self.direccion = ""

    def toString(self):
        print(self.nombre+self.delimitador+
            self.apellido1+self.delimitador+
            self.apellido2+self.delimitador+
            self.email+self.delimitador+
            self.telefono1+self.delimitador+
            self.telefono2+self.delimitador+
            self.direccion+self.delimitador
            )