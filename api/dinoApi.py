from datetime import datetime
from models.dino import Dinosaur, DinosaurModel
from utils.conversions import getJsonList
from flask import abort, make_response

dinosaurModel = DinosaurModel()


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def read_all():
    return dinosaurModel.getAll()


def readById(id):
    return dinosaurModel.searchById(id)


def search(property, value):
    return dinosaurModel.searchByProperty(property, value)


def update(id, dino):
    name = dino.get("name", None)
    dinoType = dino.get("dinoType", None)
    height = dino.get("height", None)
    length = dino.get("length", None)
    weight = dino.get("weight", None)
    diet = dino.get("diet", None)
    dinoObject = Dinosaur(
        name=name,
        dinoType=dinoType,
        height=height,
        length=length,
        weight=weight,
        diet=diet,
    )
    dinosaurModel.update(id, dinoObject)


def delete(id):
    if dinosaurModel.searchById(id):
        dinosaurModel.delete(id)
        return make_response(f"Dino with id {id} has been deleted", 200)
    else:
        abort(404, f"Dino with id {id} not found")


def create(dino):
    name = dino.get("name", None)
    dinoType = dino.get("dinoType", None)
    height = dino.get("height", None)
    length = dino.get("length", None)
    weight = dino.get("weight", None)
    diet = dino.get("diet", None)

    if name:
        dinoObject = Dinosaur(
            name=name,
            dinoType=dinoType,
            height=height,
            length=length,
            weight=weight,
            diet=diet,
        )
        dinosaurModel.insert(dinoObject)
    else:
        abort(406, f"Some error")
