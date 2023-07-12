from flask import render_template
from api.dinoApi import read_all
import connexion

from utils.dbconnect import DBConnect

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")


@app.route("/")
def index():
    dinos = read_all()
    return render_template("home.html", dinos=dinos)


# for dino using flask and templates


# @app.route("/dinolist")
# def dinos():
#     dinos = dbconnect.getAllDinos()
#     return render_template("dinos.html", dinos=dinos)


# @app.route("/dino/<id>")
# def getDinoInfo(id):
#     dinos = dbconnect.searchById(id)
#     if dinos == None:
#         return "None found"
#     else:
#         return render_template("dino.html", dinos=dinos)


# @app.route("/dinoType/<dinoType>")
# def getDinoByType(dinoType):
#     dinos = dbconnect.searchByType(dinoType)
#     if dinos == None:
#         return "None found"
#     else:
#         return render_template("dino.html", dinos=dinos)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
