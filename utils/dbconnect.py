from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import sys


class DBConnect:
    def __init__(self, uri=None):
        if uri is None:
            uri = "mongodb+srv://gsmayya:bBqbems5GrfnoONg@cluster0.nd9r0m5.mongodb.net/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi("1"))
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command("ping")
            print("Pinged your deployment. You successfully connected to MongoDB!")
            self.db = self.client["website"]
        except Exception as e:
            print(e)
            sys.exit(1)

    def setTable(self, table):
        self.table = self.db[table]

    def connect(self):
        return True

    def disconnect(self):
        return True

    def insert(self, keyValuePairs):
        self.table.insert_one(keyValuePairs)
        return True

    def update(self, id, keyValuePairs):
        myquery = {"id", id}
        self.table.update_one(myquery, keyValuePairs)

    def delete(self, id):
        myquery = {"id", id}
        self.table.delete_one(myquery)

    def search(self, key, value):
        myquery = {key: value}
        return self.table.find(myquery)

    def getall(self):
        myquery = {}
        return self.table.find(myquery)
