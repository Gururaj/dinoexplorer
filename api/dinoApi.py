from datetime import datetime
from utils.dbconnect import DBConnect
from models.dino import Dino
from utils.conversions import getJsonList
from flask import abort, make_response

dbconnect = DBConnect()


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def read_all():
    return getJsonList(dbconnect.getAllDinos())


def readById(id):
    return getJsonList(dbconnect.searchById(id))


def update(id, dino):
    name = dino.get("name", None)
    dinoType = dino.get("dinoType", None)
    height = dino.get("height", None)
    length = dino.get("length", None)
    weight = dino.get("weight", None)
    dinoObject = Dino(
        name=name, dinoType=dinoType, height=height, length=length, weight=weight
    )
    dbconnect.update(id, dinoObject)


def delete(id):
    if dbconnect.searchById(id):
        dbconnect.delete(id)
        return make_response(f"Dino with id {id} has been deleted", 200)
    else:
        abort(404, f"Dino with id {id} not found")


def create(dino):
    name = dino.get("name", None)
    dinoType = dino.get("dinoType", None)
    height = dino.get("height", None)
    length = dino.get("length", None)
    weight = dino.get("weight", None)

    if name:
        dinoObject = Dino(
            name=name, dinoType=dinoType, height=height, length=length, weight=weight
        )
        dbconnect.insert(dinoObject)
    else:
        abort(406, f"Some error")
