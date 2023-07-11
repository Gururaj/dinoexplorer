from datetime import datetime
from entities.dbconnect import DBConnect
from entities.dino import Dino
from utils import getJsonList
from flask import abort

dbconnect = DBConnect()


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def read_all():
    return getJsonList(dbconnect.getAllDinos())


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
