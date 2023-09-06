import sys
import os 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest


from entities.dinosaur import Dinosaur
from entities.dinotype import DinoType
from models.models import DinosaurModel


class TestDino:
    dino = Dinosaur("Tyrannosaurus Rex", "Carnivore", "20", "40", "8000", "Theropod")

    def test_dino_diet(self):
        assert self.dino.diet == "Carnivore"
        
    def test_dino_type(self):
        assert self.dino.dinoType == DinoType("Theropod")
        assert str(self.dino.dinoType) == "Theropod"

    # def test_all(self):
    #     dinoModel = DinosaurModel()
    #     dinos = dinoModel.getAll()
    #     assert len(dinos) > 1

    # def test_searchById(self):
    #     dinoModel = DinosaurModel()
    #     dinos = dinoModel.searchById("stegosaurus")
    #     assert len(dinos) == 1
    #     assert dinos[0].name == "Stegosaurus"
    #     assert dinos[0].diet == "Herbivore"

    # def test_searchByName(self):
    #     dinoModel = DinosaurModel()
    #     dinos = dinoModel.searchByProperty("name", "Stegosaurus")
    #     assert len(dinos) == 1
    #     assert dinos[0].name == "Stegosaurus"
    #     assert dinos[0].diet == "Herbivore"

    # def test_searchByDiet(self):
    #     dinoModel = DinosaurModel()
    #     dinos = dinoModel.searchByProperty("diet", "Herbivore")
    #     assert len(dinos) >= 1
    #     assert dinos[0].diet == "Herbivore"

    # def test_searchByType(self):
    #     dinoModel = DinosaurModel()
    #     dinos = dinoModel.searchByProperty("dinoType", "Thyreophoran")
    #     assert len(dinos) >= 1
    #     assert dinos[0].dinoType == "Thyreophoran"

class TestDinoType:
    __dinoTypes = {
        "Theropod": "theropod",
        "Sauropod": "sauropod",
        "Thyreophoran": "thyreophoran",
        "Ceratopsian": "ceratopsian",
        "Raptor": "raptor",
        "Ornithopod": "ornithopod",
    }
    def test_dinotype(self):
        for dinotype in self.__dinoTypes.keys():
            self.run_for_type(dinotype)
    
    def run_for_type(self, str):
        dinoType = DinoType(str)
        assert dinoType.dino_type == str
        assert dinoType.get_id() == str.lower()
        