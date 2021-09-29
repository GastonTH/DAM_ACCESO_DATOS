from objs import Contacto

class Agenda():

    def __init__(self):

        """
        Constructor de la clase Agenda, que, al menos en esta version solo guardara una agenda
        -POSIBLE SOLUCION AL PROBLEMA DE GUARDAR MAS DE UNA AGENDA
        [{nombre_agenda_1: nombre_del_fichero]
        -CSV.DICTWRITER() --> coge la cabecera del fichero csv y lo guarda 
        - importante guardar la cabecera de el fichero csv para el listado de ficheros
        """
        self.lista_contactos = []
    