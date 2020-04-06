import os
import json

class IndexedStore:
    def __init__(self, filePath):
        self.filePath = filePath
        self.currentIndex = 0
        self.objectDictionary = {}

        self._load()

    def add(self, object):
        object["id"] = self._next_index()
        self.objectDictionary[object["id"]] = object
        self._persist()
        return object

    def update(self, object):
        if object["id"] == None:
            raise Exception("Object to update has no id.")

        if not(object["id"] in self.objectDictionary):
            raise Exception("Object id to update does not exist.")

        self.objectDictionary[object["id"]] = object
        
        self._persist()
        return object

    def get_all(self):
        return list(self.objectDictionary.values())

    def get(self, index):
        return self.objectDictionary[index]

    def remove(self, index):
        del self.objectDictionary[index]
        self._persist()

    def _next_index(self):
        self.currentIndex += 1
        return self.currentIndex

    def _persist(self):
        with open(self.filePath, "w") as f:
            array = self.get_all()
            json.dump(array, f)

    def _load(self):
        if (not(os.path.exists(self.filePath))):
            return []

        with open(self.filePath, "r") as f:
            jsonArray = json.load(f)

        for obj in jsonArray:
            if obj["id"] in self.objectDictionary:
                raise Exception("Id {} has a duplicate".format(obj["id"]))

            self.objectDictionary[obj["id"]] = obj

        if len(self.objectDictionary) > 0:
            self.currentIndex = max(self.objectDictionary.keys())

