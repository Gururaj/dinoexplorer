
class DinoType:
    __dinoTypes = {
        "Theropod": "theropod",
        "Sauropod": "sauropod",
        "Thyreophoran": "thyreophoran",
        "Ceratopsian": "ceratopsian",
        "Raptor": "raptor",
        "Ornithopod": "ornithopod",
    }

    def __init__(self, dino_type):
        self.id = self.create_id(str(dino_type))
        self.dino_type = self.check_dino_types(str(dino_type))        

    def get_id(self):
        return self.id

    def get_type_name(self):
        return self.dino_type

    def create_id(self, dino_type):
        return self.__dinoTypes[dino_type]

    def check_dino_types(self, dino_type):
        if dino_type not in self.__dinoTypes.keys():
            raise ValueError(
                "Dino Type must be one of: " + str(self.__dinoTypes.keys())
            )
        else:
            return str(dino_type).capitalize()

    def __str__(self):
        return self.dino_type

    def __repr__(self):
        return self.dino_type


    def __eq__(self, __value):
        if __value.dino_type == self.dino_type:
            return True
        return False 