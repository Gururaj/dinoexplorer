from tinydb import TinyDB, Query, where


class DBConnect:
    def __init__(self, path=None):
        if path == None:
            path = "database/db.json"
        self.connection = TinyDB(path)
        self.table = None

    def setTable(self, table):
        self.table = self.connection.table(table)

    def connect(self):
        return True

    def disconnect(self):
        return True

    def insert(self, keyValuePairs):
        self.table.insert(keyValuePairs)
        return True

    def update(self, id, keyValuePairs):
        query = Query()
        self.table.update(keyValuePairs, query.id == id)

    def delete(self, id):
        query = Query()
        self.table.remove(query.id == id)

    def search(self, key, value):
        return self.table.search(where(key) == value)

    def getall(self):
        return self.table.all()
