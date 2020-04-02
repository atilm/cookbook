import unittest
import os
from cookbookServer.recipe import Recipe
from cookbookServer.recipeRepository import RecipeRepository

class TestRecipeRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.testFile = "test_recipe_repo.json"

    def setUp(self):
        if (os.path.exists(self.testFile)):
            os.remove(self.testFile)

    def test_save_and_get_all(self):
        saveRepo = RecipeRepository(self.testFile)
        recipeOne = self._create_default_recipe()
        recipeTwo = self._create_default_recipe()
        recipeTwo.name = "Recipe Two"

        returnedRecipeOne = saveRepo.save(recipeOne)
        returnedRecipeTwo = saveRepo.save(recipeTwo)
        
        self.assertEqual(returnedRecipeOne.id, 1)
        self.assertEqual(returnedRecipeTwo.id, 2)

        loadRepo = RecipeRepository(self.testFile)

        loadedRecipes = loadRepo.get_all()

        self.assertEqual(len(loadedRecipes), 2)
        self._assert_recipes_equal(loadedRecipes[0], returnedRecipeOne)
        self._assert_recipes_equal(loadedRecipes[1], returnedRecipeTwo)

    def test_save_raises_exception_for_object_with_id(self):
        recipe = self._create_default_recipe()
        recipe.id = 4

        repo = RecipeRepository(self.testFile)

        with self.assertRaises(Exception):
            repo.save(recipe)

    def test_get(self):
        saveRepo = RecipeRepository(self.testFile)
        recipeOne = self._create_default_recipe()
        recipeTwo = self._create_default_recipe()
        recipeTwo.name = "Recipe Two"

        returnedRecipeOne = saveRepo.save(recipeOne)
        returnedRecipeTwo = saveRepo.save(recipeTwo)

        loadRepo = RecipeRepository(self.testFile)

        self._assert_recipes_equal(loadRepo.get(returnedRecipeOne.id), returnedRecipeOne)

    def test_update(self):
        saveRepo = RecipeRepository(self.testFile)
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

        loadRepo = RecipeRepository(self.testFile)

        self.assertEqual(loadRepo.get(2).instructions, "New instructions")

    def test_delete(self):
        saveRepo = RecipeRepository(self.testFile)
        recipeOne = self._create_default_recipe()
        recipeTwo = self._create_default_recipe()
        recipeTwo.name = "Recipe Two"

        returnedRecipeOne = saveRepo.save(recipeOne)
        returnedRecipeTwo = saveRepo.save(recipeTwo)
        
        with self.assertRaises(Exception):
            saveRepo.delete(45)

        saveRepo.delete(returnedRecipeOne.id)

        loadRepo = RecipeRepository(self.testFile)

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


    