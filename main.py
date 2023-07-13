from flask import render_template
from api.dinoApi import read_all, search
import connexion

from utils.dbconnect import DBConnect

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")


@app.route("/")
def index():
    dinos = read_all()
    return render_template("home.html", dinos=dinos)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
