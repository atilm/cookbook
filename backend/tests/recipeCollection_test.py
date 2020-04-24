import unittest
import datetime
from cookbookServer.recipeCollection import RecipeCollection

class TestRecipeCollection(unittest.TestCase):
    def test_constuctor(self):
        collection = RecipeCollection()

        id = collection.id
        date = collection.date
        recipeIds = collection.recipeIds

        self.assertEqual(id, None)
        self.assertEqual(date, datetime.date.today())
        self.assertEqual(len(recipeIds), 0)

    def test_to_and_from_dict(self):
        collection = RecipeCollection()
        collection.id = 44
        collection.date = datetime.date(1999, 2, 23)
        collection.recipeIds = [13, 45, 6]

        serialized = collection.to_dict()

        resultCollection = RecipeCollection.from_dict(serialized)

        self.assertEqual(resultCollection.id, 44)
        self.assertEqual(resultCollection.date, datetime.date(1999, 2, 23))
        self.assertListEqual(resultCollection.recipeIds, [13, 45, 6])