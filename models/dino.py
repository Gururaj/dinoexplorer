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
        self.db.insert(dino.__dict__)

    def update(self, dino):
        self.db.update(dino.id, dino.__dict__)

    def delete(self, dino):
        self.db.delete(dino.id)

    def searchById(self, id):
        return self.convert(self.db.search("id", id))

    def searchByProperty(self, property, value):
        return self.convert(self.db.search(property, value))

    def convert(self, data):
        result = []
        for d in data:
            dino = Dinosaur(
                d["name"],
                d["diet"],
                d["height"],
                d["length"],
                d["weight"],
                d["dinoType"],
            )
            result.append(dino)
        return result


class Dinosaur:
    def __init__(self, name, diet, height, length, weight, dinoType):
        self.name = self.checkName(name)
        self.id = self.createId(name)
        self.diet = self.checkDiet(diet)
        # in meters
        self.height = self.checkHeight(height)
        # in meters
        self.length = self.checkLength(length)
        # in kg
        self.weight = self.checkWeight(weight)
        self.dinoType = dinoType

    def __str__(self):
        finalStr = ""
        for key, value in self.__dict__.items():
            finalStr += key + ": " + str(value) + "\n"
        return finalStr

    def __repr__(self):
        return self.__str__()

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
        dinoTypes = ["Theropod", "Sauropod", "Thyreophoran", "Ceratopsian", "Raptor"]
        if dinoType not in dinoTypes:
            raise ValueError("Dino Type must be one of: " + str(dinoTypes))
        else:
            return dinoType


# def createDinoTypeFactory():
#     def init(self, typeName):
#         self.typeName = typeName

#     def strclass(self):
#         finalStr = ""
#         for key, value in self.__dict__.items():
#             finalStr += key + ": " + str(value) + "\n"
#         return finalStr

#     def repr(self):
#         return self.__str__()

#     def getType(self):
#         return self.typeName

#     return type(
#         "DinoType",
#         (object,),
#         {
#             "__init__": init,
#             "__str__": strclass,
#             "__repr__": repr,
#             "getType": getType,
#         },
#     )
