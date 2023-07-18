class Dinosaur(dict):
    __diets = ["Carnivore", "Herbivore", "Omnivore"]

    def __init__(self, name, diet, height, length, weight, dinoType):
        dict.__init__(
            self,
            name=self.checkName(name),
            id=self.createId(name),
            diet=self.checkDiet(diet),
            height=self.checkHeight(height),
            length=self.checkLength(length),
            weight=self.checkWeight(weight),
            dinoType=self.checkDinoType(dinoType),
        )

    def fromJson(data):
        return Dinosaur(
            data["name"],
            data["diet"],
            data["height"],
            data["length"],
            data["weight"],
            data["dinoType"],
        )

    def createId(self, name):
        return name.replace(" ", "").lower()

    # Validators and convertors
    # move this later to better class
    def checkName(self, name):
        return name

    def checkDiet(self, diet):
        if diet not in self.__diets:
            raise ValueError("Diet must be one of: " + str(self.__diets))
        return diet

    def checkHeight(self, height):
        return int(height)

    def checkLength(self, length):
        return int(length)

    def checkWeight(self, weight):
        return int(weight)

    def checkDinoType(self, dinoType):
        return DinoType(dinoType)


class DinoType(dict):
    __dinoTypes = {
        "Theropod": "theropod",
        "Sauropod": "sauropod",
        "Thyreophoran": "thyreophoran",
        "Ceratopsian": "ceratopsian",
        "Raptor": "raptor",
    }

    def __init__(self, dinoType):
        dict.__init__(
            self,
            id=self.createId(str(dinoType)),
            dinoType=self.checkDinoType(str(dinoType)),
        )

    def getId(self):
        return self.id

    def getTypeName(self):
        return self.dinoType

    def createId(self, dinoType):
        return self.__dinoTypes[dinoType]

    def checkDinoType(self, dinoType):
        if dinoType not in self.__dinoTypes.keys():
            raise ValueError(
                "Dino Type must be one of: " + str(self.__dinoTypes.keys())
            )
        else:
            return dinoType.capitalize()

    def __str__(self):
        return self["dinoType"]

    def __repr__(self) -> str:
        return self["dinoType"]
