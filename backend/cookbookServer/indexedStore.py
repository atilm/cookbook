class IndexedStore:
    def __init__(self, listOfObjects):
        self.currentIndex = 0
        self.objectDictionary = {}

        for obj in listOfObjects:
            if obj.id in self.objectDictionary:
                raise Exception("Id {} has a duplicate".format(obj.id))

            self.objectDictionary[obj.id] = obj

        if len(self.objectDictionary) > 0:
            self.currentIndex = max(self.objectDictionary.keys())

    def add(self, object):
        object.id = self._next_index()
        self.objectDictionary[object.id] = object

    def get_all(self):
        return list(self.objectDictionary.values())

    def get(self, index):
        return self.objectDictionary[index]

    def remove(self, index):
        del self.objectDictionary[index]

    def _next_index(self):
        self.currentIndex += 1
        return self.currentIndex

