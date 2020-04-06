import unittest
import os
from tests.testConfig import TestConfig
from cookbookServer.storeManager import StoreManager
from cookbookServer.food import Food
from cookbookServer.foodRepository import FoodRepository

class TestFoodRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = TestConfig()

    def setUp(self):
        if (os.path.exists(self.config.FOOD_REPOSITORY)):
            os.remove(self.config.FOOD_REPOSITORY)
        # overwrite paths to data files and reset stores
        manager = StoreManager(self.config)
        manager.setConfig(self.config)

    def test_save_and_get_all(self):
        saveRepo = FoodRepository(self.config)
        foodOne = self.__createFood("foodOne")
        foodTwo = self.__createFood("foodTwo")

        returnedFoodOne = saveRepo.Save(foodOne)
        returnedFoodTwo = saveRepo.Save(foodTwo)

        self.assertEqual(returnedFoodOne.id, 1)
        self.assertEqual(returnedFoodTwo.id, 2)

        loadRepo = FoodRepository(self.config)

        loadedFood = loadRepo.GetAll()

        self.assertEqual(len(loadedFood), 2)
        self.__assert_food_equal(loadedFood[0], returnedFoodOne)
        self.__assert_food_equal(loadedFood[1], returnedFoodTwo)

    def __createFood(self, name):
        return Food(name, 1, ["Jan", "Feb"])

    def __assert_food_equal(self, foodA, foodB):
        self.assertEqual(foodA.id, foodB.id)
        self.assertEqual(foodA.name, foodB.name)
        self.assertEqual(foodA.kcal, foodB.kcal)
        self.assertEqual(foodA.seasonMonths, foodB.seasonMonths)