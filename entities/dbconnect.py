from tinydb import TinyDB, Query
from entities.dino import Dino


class DBConnect:
    def __init__(self):
        self.connection = TinyDB("database/db.json")
        self.dino = self.connection.table("dino")

    def connect(self):
        return True

    def disconnect(self):
        return True

    def insert(self, dino):
        self.dino.insert(dino.__dict__)
        return True

    def searchById(self, id):
        query = Query()
        result = self.convert(self.dino.search(query.id == id))
        return result

    def convert(self, data):
        result = []
        for d in data:
            dino = Dino(d["name"], d["dinoType"], d["height"], d["length"], d["weight"])
            result.append(dino)
        return result

    def searchByName(self, name):
        query = Query()
        result = self.convert(self.dino.search(query.name == name))
        return result

    def getAllDinos(self):
        query = Query()
        result = self.convert(self.dino.all())
        return result
