import unittest
from cookbookServer.indexedStore import IndexedStore

class IdObject:
    def __init__(self, id):
        self.id = id

class TestIndexedStore(unittest.TestCase):
    def test_constructor_and_get_all(self):
        objects = [IdObject(13), IdObject(14)]

        store = IndexedStore(objects)

        self.assertEqual(len(store.get_all()), 2)
        self.assertEqual(store.get(13).id, 13)
        self.assertEqual(store.get(14).id, 14)

    def test_constructor_raises_exception_when_ids_not_unique(self):
        objects = [IdObject(13), IdObject(14), IdObject(14)]

        with self.assertRaises(Exception):
            IndexedStore(objects)

    def test_get(self):
        objects = [IdObject(13), IdObject(14), IdObject(17)]

        store = IndexedStore(objects)

        self.assertEqual(store.get(14), objects[1])

    def test_add(self):
        store = IndexedStore([])
        returnedObject = store.add(IdObject(None))

        self.assertEqual(returnedObject.id, 1)

        self.assertEqual(len(store.get_all()), 1)
        self.assertEqual(store.get(1).id, 1)

        store.add(IdObject(None))

        self.assertEqual(store.get(2).id, 2)

    def test_add_after_loading_data(self):
        objects = [IdObject(1), IdObject(5), IdObject(14)]

        store = IndexedStore(objects)
        store.add(IdObject(None))
        self.assertEqual(store.get(15).id, 15)

    def test_delete_object(self):
        objects = [IdObject(1), IdObject(5), IdObject(14)]
        store = IndexedStore(objects)
        store.remove(5)
        self.assertEqual(len(store.get_all()), 2)
        self.assertEqual(store.get(1).id, 1)
        self.assertEqual(store.get(14).id, 14)