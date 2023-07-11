class Dino:
    def __init__(self, name, dinoType, height, length, weight):
        self.name = name
        self.id = self.createId(name)
        self.dinoType = dinoType
        self.height = height
        self.length = length
        self.weight = weight

    def __str__(self):
        return (
            "ID:"
            + self.id
            + "\nName: "
            + self.name
            + "\nType: "
            + self.dinoType
            + "\nHeight: "
            + self.height
            + "\nLength: "
            + self.length
            + "\nWeight: "
            + self.weight
            + "\n"
        )

    def __repr__(self):
        return self.__str__()

    def getJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "dinoType": self.dinoType,
            "height": self.height,
            "length": self.length,
            "weight": self.weight,
        }

    def createId(self, name):
        return name.replace(" ", "").lower()
