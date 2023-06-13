class Database:
    def __init__(self, database_template) :
        self.database = []
        dispositivos = database_template.get("dispositivos")
        for dispositivo in dispositivos:
            self.database.append(Dispositivo(diccionario = dispositivo))
            
    def delete_by_id(self, id):
        for dispositivo in self.database:
            if dispositivo.id == id:
                self.database.remove(dispositivo)

    def add_dispositivo(self, dispositivo = '', diccionario = ''):
        if dispositivo:
            self.database.append(dispositivo)
        if diccionario:
            self.database.append(Dispositivo(diccionario=diccionario))

class Dispositivo:
    def __init__(self, id = None, nombre = None, marca = None, tipo = None, diccionario = None):
        self.id = id
        self.nombre = nombre
        self.marca = marca
        self.tipo = tipo

        if diccionario:
            self.id = diccionario.get("id")
            self.nombre = diccionario.get("nombre")
            self.marca = diccionario.get("marca")
            self.tipo = diccionario.get("tipo")
            