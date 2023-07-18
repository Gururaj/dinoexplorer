from utils.dbconnect import DBConnect
from tinydb import Query
from dino import Dinosaur, DinoType


class DinosaurModel:
    tableNames = {
        "Dinosaur": "dino",
        "DinoType": "dinoType",
    }

    def __init__(self, db=None):
        if db == None:
            self.db = DBConnect()
        else:
            self.db = db

    def setDB(self, entity):
        self.db.setTable(self.tableNames[entity])

    def getAll(self):
        return self.convert(self.db.getall())

    def insert(self, dino):
        self.db.insert(self.keyValuePairs(dino))

    def update(self, dino):
        self.db.update(dino.id, self.keyValuePairs(dino))

    def delete(self, dino):
        self.db.delete(dino.id)

    def searchById(self, id):
        return self.convert(self.db.search("id", id))

    def searchByProperty(self, property, value):
        return self.convert(self.db.search(property, value))

    def keyValuePairs(self, dino):
        keyValuePairs = {}
        for key in dino.keys():
            keyValuePairs[key] = str(dino[key])
        return keyValuePairs

    def convert(self, data):
        dinoList = []
        for d in data:
            dinoList.append(Dinosaur.fromJson(d))
        return dinoList
