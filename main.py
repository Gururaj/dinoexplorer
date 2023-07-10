from flask import Flask, redirect, url_for, request, render_template

# from getDinoList import getDinoList, getDinoFromId
from entities.dbconnect import DBConnect
from entities.dino import Dino

app = Flask(__name__, template_folder="templates", static_folder="statics")
dbconnect = DBConnect()


@app.route("/test")
def index():
    return render_template("index.html")


@app.route("/")
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


if __name__ == "__main__":
    app.run(debug=True)
