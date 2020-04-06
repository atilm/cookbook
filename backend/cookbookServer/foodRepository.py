from cookbookServer.food import Food
from cookbookServer.config import Config
from os import path
import json

class FoodRepository:
    def __init__(self, config):
        self.foodStore = {}
        self.currentId = 0
        self.filePath = config.FOOD_REPOSITORY
        self._load()

    def Save(self, food):
        newId = self._nextId()
        self.foodStore[newId] = food
        food.id = newId
        self._persist()
        return food
    
    def Update(self, food):
        if food.id == None:
            raise Exception("Object to update has no id.")

        if not (food.id in self.foodStore):
            raise Exception("Object id to update does not exist.")

        self.foodStore[food.id] = food
        self._persist()
        return self.foodStore[food.id]

    def GetAll(self):
        return list(self.foodStore.values())

    def GetBySearchTerm(self, search_term):
        return filter(lambda food: search_term in food.name, self.foodStore.values())

    def GetById(self, id):
        if not(id in self.foodStore):
            return Food(None, None, [])

        return self.foodStore[id]

    def Delete(self, id):
        if not(id in self.foodStore):
            raise Exception("Given id does not exist")
        
        del self.foodStore[id]
        self._persist()

    def _persist(self):
        with open(self.filePath, "w") as f:
            foodList = list(map(lambda i: i.to_dict(), self.GetAll()))
            json.dump(foodList, f)

    def _load(self):
        if (not(path.exists(self.filePath))):
            return

        with open(self.filePath, "r") as f:
            jsonArray = json.load(f)
            
        self.foodStore = dict((js['id'], Food.fromJson(js)) for js in jsonArray)
        self.currentId = max(self.foodStore.keys())

    def _nextId(self):
        self.currentId += 1
        return self.currentId
        


