import unittest
import os
import json
from tests.testConfig import TestConfig
from cookbookServer.database.indexedStore import IndexedStore

class TestIndexedStore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.testFile = os.path.join(TestConfig.DATABASE_FOLDER, "indexed_store_test_repo.json")

    def setUp(self):
        if (os.path.exists(self.testFile)):
            os.remove(self.testFile)

    def __createObj(self, id):
        return { "id": id}

    def __fillTestFile(self, arrayOfIds):
        data = [self.__createObj(id) for id in arrayOfIds]

        with open(self.testFile, "w") as f:
            json.dump(data, f)

    def test_constructor_and_get_all(self):
        self.__fillTestFile([13, 14])

        store = IndexedStore(self.testFile)

        self.assertEqual(len(store.get_all()), 2)
        self.assertEqual(store.get(13)["id"], 13)
        self.assertEqual(store.get(14)["id"], 14)

    def test_constructor_raises_exception_when_ids_not_unique(self):
        self.__fillTestFile([13, 14, 14])

        with self.assertRaises(Exception):
            IndexedStore(self.testFile)

    def test_get(self):
        self.__fillTestFile([13, 14, 17])

        store = IndexedStore(self.testFile)

        self.assertEqual(store.get(14)["id"], 14)

    def test_add(self):
        store = IndexedStore(self.testFile)
        returnedObject = store.add(self.__createObj(None))

        self.assertEqual(returnedObject["id"], 1)

        self.assertEqual(len(store.get_all()), 1)
        self.assertEqual(store.get(1)["id"], 1)

        store.add(self.__createObj(None))

        self.assertEqual(store.get(2)["id"], 2)

    def test_add_after_loading_data(self):
        self.__fillTestFile([1, 5, 14])

        store = IndexedStore(self.testFile)
        store.add(self.__createObj((None)))
        self.assertEqual(store.get(15)["id"], 15)

    def test_delete_object(self):
        self.__fillTestFile([1, 5, 14])

        store = IndexedStore(self.testFile)
        store.remove(5)
        self.assertEqual(len(store.get_all()), 2)
        self.assertEqual(store.get(1)["id"], 1)
        self.assertEqual(store.get(14)["id"], 14)