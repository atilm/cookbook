import unittest
import os
from tests.testConfig import TestConfig
from cookbookServer.database.storeManager import StoreManager
from cookbookServer.food import Food
from cookbookServer.recipe import Recipe
from cookbookServer.foodService import FoodRepository
from cookbookServer.recipeRepository import RecipeRepository

class TestRepositoryInterdependence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = TestConfig()

    def setUp(self):
        self.__reset_test_data(self.config.FOOD_REPOSITORY)
        self.__reset_test_data(self.config.RECIPE_REPOSITORY)
        # overwrite paths to data files and reset stores
        manager = StoreManager(self.config)
        manager.setConfig(self.config)

    def test_when_food_is_renamed_references_in_recipes_are_updated(self):
        # Arrange
        foodRepo = FoodRepository(self.config)
        recipeRepo = RecipeRepository(self.config)

        cream = foodRepo.Save(Food("Schlagobers", 220, []))
        
        plateOfCream = Recipe()
        plateOfCream.name = "Plate of cream"
        plateOfCream.add_ingredient(cream.id, cream.name, 200, "g")

        plateOfCream = recipeRepo.save(plateOfCream)

        # Act
        cream.name = "Schlagsahne"
        foodRepo.Update(cream)

        # Assert
        updatedRecipe = recipeRepo.get(plateOfCream.id)
        self.assertEqual(updatedRecipe.ingredients[0]["food"]["name"], "Schlagsahne")

    def __reset_test_data(self, filePath):
        if (os.path.exists(filePath)):
            os.remove(filePath)