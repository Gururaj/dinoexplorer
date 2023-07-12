import pytest

from dino import Dinosaur, DinosaurModel
from utils.dbconnect import DBConnect


class TestDino:
    def test_dino(self):
        dino = Dinosaur(
            "Tyrannosaurus Rex", "Carnivore", "20", "40", "8000", "Theropod"
        )
        assert dino.diet == "Carnivore"

    def test_all(self):
        dinoModel = DinosaurModel()
        dinos = dinoModel.getAll()
        assert len(dinos) > 1

    def test_searchById(self):
        dinoModel = DinosaurModel()
        dinos = dinoModel.searchById("stegosaurus")
        assert len(dinos) == 1
        assert dinos[0].name == "Stegosaurus"
        assert dinos[0].diet == "Herbivore"

    def test_searchByName(self):
        dinoModel = DinosaurModel()
        dinos = dinoModel.searchByProperty("name", "Stegosaurus")
        assert len(dinos) == 1
        assert dinos[0].name == "Stegosaurus"
        assert dinos[0].diet == "Herbivore"

    def test_searchByDiet(self):
        dinoModel = DinosaurModel()
        dinos = dinoModel.searchByProperty("diet", "Herbivore")
        assert len(dinos) >= 1
        assert dinos[0].diet == "Herbivore"

    def test_searchByType(self):
        dinoModel = DinosaurModel()
        dinos = dinoModel.searchByProperty("dinoType", "Thyreophoran")
        assert len(dinos) >= 1
        assert dinos[0].dinoType == "Thyreophoran"
