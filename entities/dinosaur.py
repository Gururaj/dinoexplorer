from entities.dinotype import DinoType

class Dinosaur:
    __diets = ["Carnivore", "Herbivore", "Omnivore"]    

    def __init__(self, name, diet, height, length, weight, dinoType):
        self.name=self.checkName(name)
        self.id=self.createId(name)
        self.diet=self.checkDiet(diet)
        self.height=self.checkHeight(height)
        self.length=self.checkLength(length)
        self.weight=self.checkWeight(weight)
        self.dinoType=self.checkDinoType(dinoType)        
    
    def __dict__(self):
        return {
            "id": self.id,
            "name": self.name, 
            "diet": self.diet, 
            "height": self.height, 
            "length": self.length, 
            "weight": self.weight,
            "dinoType": self.dinoType.__str__()
        }

    def to_json(self, data): 
        return self.__dict__()

    def from_json(self, data):
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


if __name__ == "__main__":
    print("Works")