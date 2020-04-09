import unittest
import os
from tests.testConfig import TestConfig
from cookbookServer.database.storeManager import StoreManager
from cookbookServer.recipe import Recipe
from cookbookServer.recipeRepository import RecipeRepository

class TestRecipeRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = TestConfig()

    def setUp(self):
        if (os.path.exists(self.config.RECIPE_REPOSITORY)):
            os.remove(self.config.RECIPE_REPOSITORY)
        # overwrite paths to data files and reset stores
        manager = StoreManager(self.config)
        manager.setConfig(self.config)

    def test_save_and_get_all(self):
        saveRepo = RecipeRepository(self.config)
        recipeOne = self._create_default_recipe()
        recipeTwo = self._create_default_recipe()
        recipeTwo.name = "Recipe Two"

        returnedRecipeOne = saveRepo.save(recipeOne)
        returnedRecipeTwo = saveRepo.save(recipeTwo)
        
        self.assertEqual(returnedRecipeOne.id, 1)
        self.assertEqual(returnedRecipeTwo.id, 2)

        loadRepo = RecipeRepository(self.config)

        loadedRecipes = loadRepo.get_all()

        self.assertEqual(len(loadedRecipes), 2)
        self._assert_recipes_equal(loadedRecipes[0], returnedRecipeOne)
        self._assert_recipes_equal(loadedRecipes[1], returnedRecipeTwo)

    def test_save_raises_exception_for_object_with_id(self):
        recipe = self._create_default_recipe()
        recipe.id = 4

        repo = RecipeRepository(self.config)

        with self.assertRaises(Exception):
            repo.save(recipe)

    def test_get(self):
        saveRepo = RecipeRepository(self.config)
        recipeOne = self._create_default_recipe()
        recipeTwo = self._create_default_recipe()
        recipeTwo.name = "Recipe Two"

        returnedRecipeOne = saveRepo.save(recipeOne)
        returnedRecipeTwo = saveRepo.save(recipeTwo)

        loadRepo = RecipeRepository(self.config)

        self._assert_recipes_equal(loadRepo.get(returnedRecipeOne.id), returnedRecipeOne)

    def test_get_by_search_term(self):
        recipe1 = self.__create_recipe(name="Auberginenschnitzel", ingredients=["Aubergine", "Ei", "Mehl"])
        recipe2 = self.__create_recipe(name="Der Imam fällt in ohnmacht", ingredients=["auberginen", "Zucchini", "Feta", "Tomate"])
        recipe3 = self.__create_recipe(name="Should not be found", ingredients=["Butter", "Zucker"], tags=["ohne Aubergine"])

        repo = RecipeRepository(self.config)
        repo.save(recipe1)
        repo.save(recipe2)
        repo.save(recipe3)

        results = repo.get_by_search_term("aubergine")

        self.assertEqual(len(results), 2)

    def test_update(self):
        saveRepo = RecipeRepository(self.config)
        recipeOne = self._create_default_recipe()
        recipeTwo = self._create_default_recipe()
        recipeTwo.name = "Recipe Two"

        returnedRecipeOne = saveRepo.save(recipeOne)
        returnedRecipeTwo = saveRepo.save(recipeTwo)

        with self.assertRaises(Exception):
            saveRepo.update(Recipe())
            
        with self.assertRaises(Exception):
            recipeOne.id = 3
            saveRepo.update(recipeOne)

        returnedRecipeTwo.instructions = "New instructions"
        saveRepo.update(returnedRecipeTwo)

        loadRepo = RecipeRepository(self.config)

        self.assertEqual(loadRepo.get(2).instructions, "New instructions")

    def test_delete(self):
        saveRepo = RecipeRepository(self.config)
        recipeOne = self._create_default_recipe()
        recipeTwo = self._create_default_recipe()
        recipeTwo.name = "Recipe Two"

        returnedRecipeOne = saveRepo.save(recipeOne)
        returnedRecipeTwo = saveRepo.save(recipeTwo)
        
        with self.assertRaises(Exception):
            saveRepo.delete(45)

        saveRepo.delete(returnedRecipeOne.id)

        loadRepo = RecipeRepository(self.config)

        self.assertEqual(len(loadRepo.get_all()), 1)
        self._assert_recipes_equal(loadRepo.get(returnedRecipeTwo.id), returnedRecipeTwo)

    def _assert_recipes_equal(self, recipeA, recipeB):
        self.assertEqual(recipeA.id, recipeB.id)
        self.assertEqual(recipeA.name, recipeB.name)
        self.assertEqual(recipeA.numberOfPeople, recipeB.numberOfPeople)
        self.assertEqual(recipeA.tags, recipeB.tags)
        self.assertEqual(recipeA.ingredients, recipeB.ingredients)
        self.assertEqual(recipeA.instructions, recipeB.instructions)

    def _create_default_recipe(self):
        recipe = Recipe()
        recipe.name = "The Recipe Name"
        recipe.numberOfPeople = 4
        recipe.tags = ["Main course", "vegetarian"]
        recipe.add_ingredient(1, "Rice", 200, "g")
        recipe.add_ingredient(2, "Water", 150, "ml")
        recipe.instructions = "Cook it."
        return recipe

    def __create_recipe(self, name = "The recipe name", ingredients = [], tags = []):
        recipe = Recipe()
        recipe.name = name
        recipe.numberOfPeople = 4
        recipe.tags = tags

        for index, ingredient in enumerate(ingredients):
            recipe.add_ingredient(index, ingredient, 100 + index, "g")

        recipe.instructions = "Cook it."
        return recipe


    