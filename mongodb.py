from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://gsmayya:bBqbems5GrfnoONg@cluster0.nd9r0m5.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))
# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

mydb = client["website"]
mycoll = mydb["dinoexplorer"]


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

for dino in dinos:
    x = mycoll.insert_one(dino)
