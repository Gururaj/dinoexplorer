from utils.dbconnect import DBConnect
from models.dino import Dino


def testDB():
    dbconnect = DBConnect()
    resetData(dbconnect)
    print(dbconnect.searchById("triceratops"))
    print(dbconnect.getAllDinos())


def getMockData():
    dinos = [
        {
            "name": "Sauroposiden",
            "dinoType": "Herbivore",
            "height": "89ft",
            "length": "112ft",
            "weight": "66 tons",
        },
        {
            "name": "Tyrannosaurus Rex",
            "dinoType": "Carnivore",
            "height": "20ft",
            "length": "40ft",
            "weight": "8 tons",
        },
        {
            "name": "Velociraptor",
            "dinoType": "Carnivore",
            "height": "1.5ft",
            "length": "6ft",
            "weight": "33lbs",
        },
        {
            "name": "Triceratops",
            "dinoType": "Herbivore",
            "height": "10ft",
            "length": "30ft",
            "weight": "12 tons",
        },
        {
            "name": "Stegosaurus",
            "dinoType": "Herbivore",
            "height": "9ft",
            "length": "30ft",
            "weight": "6 tons",
        },
        {
            "name": "Brachiosaurus",
            "dinoType": "Herbivore",
            "height": "40ft",
            "length": "85ft",
            "weight": "50 tons",
        },
    ]

    dinoList = []
    for d in dinos:
        dino = Dino(d["name"], d["dinoType"], d["height"], d["length"], d["weight"])
        dinoList.append(dino)
    return dinoList


def resetData(dbconnect):
    dbconnect.connection.drop_table("dino")
    dbconnect.dino = dbconnect.connection.table("dino")
    mock = getMockData()
    for m in mock:
        dbconnect.insert(m)


if __name__ == "__main__":
    testDB()
