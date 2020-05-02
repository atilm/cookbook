import unittest
import copy
from cookbookServer.recipe import Recipe

class TestRecipe(unittest.TestCase):
    def test_to_and_from_dict(self):
        recipe = Recipe()
        recipe.id = 3
        recipe.name = "Pizza"
        recipe.numberOfPeople = 4
        recipe.tags = ["Italian", "Main Course"]
        recipe.add_ingredient(4, "flour", 200, "g")
        recipe.add_ingredient(5, "water", 200, "ml")
        recipe.instructions = "Mix it all and bake it."

        d = recipe.to_dict()

        restoredRecipe = Recipe.from_dict(d)

        self.assertEqual(restoredRecipe.id, recipe.id)
        self.assertEqual(restoredRecipe.name, recipe.name)
        self.assertEqual(restoredRecipe.numberOfPeople, 4)
        self.assertEqual(restoredRecipe.tags, recipe.tags)
        self.assertEqual(restoredRecipe.ingredients, recipe.ingredients)
        self.assertEqual(restoredRecipe.instructions, recipe.instructions)

    def test_scale_recipe(self):
        recipe = Recipe()
        recipe.id = 3
        recipe.name = "Custard"
        recipe.numberOfPeople = 4
        recipe.add_ingredient(1, "Milk", 500, "ml")
        recipe.add_ingredient(2, "Flour", 100, "g")
        recipe.add_ingredient(3, "Egg", 1, "Piece")
        recipe.add_ingredient(4, "Vanilla Bean", 1, "Piece")
        recipe.instructions = "Cook it."

        scaledRecipe = recipe.get_scaled(3)

        expectedRecipe = copy.deepcopy(recipe)
        expectedRecipe.ingredients = []
        expectedRecipe.add_ingredient(1, "Milk", 500. / 4. * 3, "ml")
        expectedRecipe.add_ingredient(2, "Flour", 100. / 4. * 3, "g")
        expectedRecipe.add_ingredient(3, "Egg", 1. / 4. * 3, "Piece")
        expectedRecipe.add_ingredient(4, "Vanilla Bean", 1. / 4. * 3, "Piece")

        self.__assert_recipes_equal__(scaledRecipe, expectedRecipe)


    def __assert_recipes_equal__(self, recipeA, recipeB):
        self.assertEqual(recipeA.id, recipeB.id)
        self.assertEqual(recipeA.name, recipeB.name)
        self.assertEqual(recipeA.numberOfPeople, recipeB.numberOfPeople)
        self.assertEqual(recipeA.tags, recipeB.tags)
        self.assertEqual(len(recipeA.ingredients), len(recipeB.ingredients))

        for index in range(len(recipeA.ingredients)):
            self.__assert_ingredients_equal__(recipeA.ingredients[index], recipeB.ingredients[index])

        self.assertEqual(recipeA.instructions, recipeB.instructions)

    def __assert_ingredients_equal__(self, ingredientA, ingredientB):
        self.assertEqual(ingredientA["food"], ingredientB["food"])
        self.assertEqual(ingredientA["unit"], ingredientB["unit"])
        self.assertAlmostEqual(ingredientA["amount"], ingredientB["amount"])