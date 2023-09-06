import sys
import os 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from entities.dinosaur import Dinosaur
from entities.dinotype import DinoType
from utils.dbconnect import DBConnect
from models.models import DinosaurModel


def testDB():
    db = DBConnect()
    resetData(db)


def resetData(db):
    # Let's do delete later.
    # Delete happens in model for each entity
    # db.connection.drop_table("dino")
    mock = getMockData()
    dinoModel = DinosaurModel(db)
    dinoModel.setDB("Dinosaur")
    for m in mock:
        dinoModel.insert(m)


def getMockData():
    dinos = [
        {
            "name": "Sauroposiden",
            "diet": "Herbivore",
            "height": "27",
            "length": "34",
            "weight": "66000",
            "dinoType": "Sauropod",
        },
        {
            "name": "Tyrannosaurus Rex",
            "diet": "Carnivore",
            "height": "6",
            "length": "12",
            "weight": "8000",
            "dinoType": "Theropod",
        },
        {
            "name": "Velociraptor",
            "diet": "Carnivore",
            "height": "1",
            "length": "2",
            "weight": "15",
            "dinoType": "Raptor",
        },
        {
            "name": "Triceratops",
            "diet": "Herbivore",
            "height": "3",
            "length": "9",
            "weight": "12000",
            "dinoType": "Ceratopsian",
        },
        {
            "name": "Stegosaurus",
            "diet": "Herbivore",
            "height": "3",
            "length": "9",
            "weight": "6000",
            "dinoType": "Thyreophoran",
        },
        {
            "name": "Brachiosaurus",
            "diet": "Herbivore",
            "height": "12",
            "length": "26",
            "weight": "50000",
            "dinoType": "Sauropod",
        },
    ]

    dinoList = []
    for d in dinos:
        dinoList.append(Dinosaur.fromJson(d))
    return dinoList


if __name__ == "__main__":
    # testDB()
    print("All imports works")
