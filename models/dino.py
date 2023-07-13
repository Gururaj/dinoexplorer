from utils.dbconnect import DBConnect
from tinydb import Query


class DinosaurModel:
    def __init__(self, db=None):
        if db == None:
            self.db = DBConnect()
            self.db.setTable("dino")
        else:
            self.db = db

    def getAll(self):
        return self.convert(self.db.getall())

    def insert(self, dino):
        self.db.insert(dino)

    def update(self, dino):
        self.db.update(dino.id, dino.__dict__)

    def delete(self, dino):
        self.db.delete(dino.id)

    def searchById(self, id):
        return self.convert(self.db.search("id", id))

    def searchByProperty(self, property, value):
        return self.convert(self.db.search(property, value))

    def convert(self, data):
        dinoList = []
        for d in data:
            dinoList.append(Dinosaur.fromJson(d))
        return dinoList


class Dinosaur(dict):
    def __init__(self, name, diet, height, length, weight, dinoType):
        dict.__init__(
            self,
            name=self.checkName(name),
            id=self.createId(name),
            diet=self.checkDiet(diet),
            height=self.checkHeight(height),
            length=self.checkLength(length),
            weight=self.checkWeight(weight),
            dinoType=self.checkDinoType(dinoType),
        )

    def fromJson(data):
        return Dinosaur(
            data["name"],
            data["diet"],
            data["height"],
            data["length"],
            data["weight"],
            data["dinoType"],
        )

    def createId(self, name):
        return name.replace(" ", "").lower()

    # Validators and convertors
    # move this later to better class
    def checkName(self, name):
        return name

    def checkDiet(self, diet):
        diets = ["Carnivore", "Herbivore", "Omnivore"]
        if diet not in diets:
            raise ValueError("Diet must be one of: " + str(diets))
        return diet

    def checkHeight(self, height):
        return int(height)

    def checkLength(self, length):
        return int(length)

    def checkWeight(self, weight):
        return int(weight)

    def checkDinoType(self, dinoType):
        return DinoType(dinoType)


class DinoType(dict):
    dinoTypes = ["theropod", "sauropod", "thyreophoran", "ceratopsian", "raptor"]

    def __init__(self, dinoType):
        dict.__init__(self, dinoType=self.checkDinoType(str(dinoType)))

    def checkDinoType(self, dinoType):
        if dinoType.lower() not in self.dinoTypes:
            raise ValueError("Dino Type must be one of: " + str(self.dinoTypes))
        else:
            return dinoType.capitalize()

    def __str__(self):
        return self["dinoType"]
