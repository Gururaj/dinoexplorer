import pytest

from dino import Dinosaur, DinosaurModel
from utils.dbconnect import DBConnect


class TestDino:
    def test_dino(self):
        dino = Dinosaur(
            "Tyrannosaurus Rex", "Carnivore", "20", "40", "8000", "Theropod"
        )
        assert dino.diet == "Carnivore"
        dinoModel = DinosaurModel()
        print(dinoModel.getAll())
