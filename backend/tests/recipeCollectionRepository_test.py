import unittest
import os
from tests.testConfig import TestConfig
from datetime import date
from cookbookServer.recipeCollectionRepository import RecipeCollectionRepository
from cookbookServer.recipeCollection import RecipeCollection
from cookbookServer.database.storeManager import StoreManager

class TestRecipeCollectionRepository(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = TestConfig()

    def setUp(self):
        if (os.path.exists(self.config.RECIPE_COLLECTION_REPOSITORY)):
            os.remove(self.config.RECIPE_COLLECTION_REPOSITORY)
        # overwrite paths to data files and reset stores
        manager = StoreManager(self.config)
        manager.setConfig(self.config)

    def test_save_and_get_all(self):
        collectionOne = self.__build_collection__(date(2020, 4, 7), [7, 34, 1])
        collectionTwo = self.__build_collection__(date(2020, 7, 9), [])

        repository = RecipeCollectionRepository(self.config)
        returnedCollectionOne = repository.save(collectionOne)
        returnedCollectionTwo = repository.save(collectionTwo)

        loadRepository = RecipeCollectionRepository(self.config)
        allCollections = loadRepository.get_all()

        self.assertEqual(returnedCollectionOne.id, 1)
        self.assertEqual(returnedCollectionTwo.id, 2)
        self.assertEqual(len(allCollections), 2)
        self.__assert_collections_equal(allCollections[0], returnedCollectionOne)
        self.__assert_collections_equal(allCollections[1], returnedCollectionTwo)

    def __build_collection__(self, date, recipeIds):
        c = RecipeCollection()
        c.date = date
        c.recipeIds = recipeIds
        return c

    def __assert_collections_equal(self, collectionA, collectionB):
        self.assertEqual(collectionA.id, collectionB.id)
        self.assertEqual(collectionA.date, collectionB.date)
        self.assertListEqual(collectionA.recipeIds, collectionB.recipeIds)
