from flask import render_template
import connexion


# from getDinoList import getDinoList, getDinoFromId
from entities.dbconnect import DBConnect
from entities.dino import Dino
from utils import getJsonList

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

dbconnect = DBConnect()


@app.route("/")
def index():
    return render_template("home.html")


# for dino using flask and templates


@app.route("/dinolist")
def dinos():
    dinos = dbconnect.getAllDinos()
    return render_template("dinos.html", dinos=dinos)


@app.route("/dino/<id>")
def getDinoInfo(id):
    dinos = dbconnect.searchById(id)
    if dinos == None:
        return "None found"
    else:
        return render_template("dino.html", dinos=dinos)


@app.route("/dinoType/<dinoType>")
def getDinoByType(dinoType):
    dinos = dbconnect.searchByType(dinoType)
    if dinos == None:
        return "None found"
    else:
        return render_template("dino.html", dinos=dinos)


# below are the api versions of above to create a restful api


@app.route("/api/dino/<id>")
def getDinoInfoApi(id):
    dinos = dbconnect.searchById(id)
    return getJsonList(dinos)


@app.route("/api/dinoType/<dinoType>")
def getDinoByTypeApi(dinoType):
    dinos = dbconnect.searchByType(dinoType)
    return getJsonList(dinos)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
