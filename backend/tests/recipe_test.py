import unittest
from cookbookServer.recipe import Recipe

class TestRecipe(unittest.TestCase):
    def test_to_and_from_dict(self):
        recipe = Recipe()
        recipe.id = 3
        recipe.name = "Pizza"
        recipe.tags = ["Italian", "Main Course"]
        recipe.add_ingredient(4, "flour", 200, "g")
        recipe.add_ingredient(5, "water", 200, "ml")
        recipe.instructions = "Mix it all and bake it."

        d = recipe.to_dict()

        restoredRecipe = Recipe.from_dict(d)

        self.assertEqual(restoredRecipe.id, recipe.id)
        self.assertEqual(restoredRecipe.name, recipe.name)
        self.assertEqual(restoredRecipe.tags, recipe.tags)
        self.assertEqual(restoredRecipe.ingredients, recipe.ingredients)
        self.assertEqual(restoredRecipe.instructions, recipe.instructions)
