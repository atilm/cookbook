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

    def test_save_raises_exception_for_object_with_id(self):
        food = self.__createFood("foodName")
        food.id = 4

        repo = FoodRepository(self.config)

        with self.assertRaises(Exception):
            repo.save(food)

    def test_get(self):
        saveRepo = FoodRepository(self.config)
        foodOne = self.__createFood("foodOne")
        foodTwo = self.__createFood("foodTwo")

        returnedFoodOne = saveRepo.Save(foodOne)
        returnedFoodTwo = saveRepo.Save(foodTwo)

        loadRepo = FoodRepository(self.config)

        self.__assert_food_equal(loadRepo.GetById(returnedFoodOne.id), returnedFoodOne)

    def test_update(self):
        saveRepo = FoodRepository(self.config)
        foodOne = self.__createFood("foodOne")
        foodTwo = self.__createFood("foodTwo")

        returnedFoodOne = saveRepo.Save(foodOne)
        returnedFoodTwo = saveRepo.Save(foodTwo)

        with self.assertRaises(Exception):
            saveRepo.Update(Food())
            
        with self.assertRaises(Exception):
            foodOne.id = 3
            saveRepo.Update(foodOne)

        returnedFoodTwo.kcal = 1234
        saveRepo.Update(returnedFoodTwo)

        loadRepo = FoodRepository(self.config)

        self.assertEqual(loadRepo.GetById(2).kcal, 1234)

    def test_delete(self):
        saveRepo = FoodRepository(self.config)
        foodOne = self.__createFood("foodOne")
        foodTwo = self.__createFood("foodTwo")

        returnedFoodOne = saveRepo.Save(foodOne)
        returnedFoodTwo = saveRepo.Save(foodTwo)
        
        with self.assertRaises(Exception):
            saveRepo.Delete(45)

        saveRepo.Delete(returnedFoodOne.id)

        loadRepo = FoodRepository(self.config)

        self.assertEqual(len(loadRepo.GetAll()), 1)
        self.__assert_food_equal(loadRepo.GetById(returnedFoodTwo.id), returnedFoodTwo)

    def __createFood(self, name):
        return Food(name, 1, ["Jan", "Feb"])

    def __assert_food_equal(self, foodA, foodB):
        self.assertEqual(foodA.id, foodB.id)
        self.assertEqual(foodA.name, foodB.name)
        self.assertEqual(foodA.kcal, foodB.kcal)
        self.assertEqual(foodA.seasonMonths, foodB.seasonMonths)