from backend.food import Food
from backend.config import Config
from os import path
import json

class FoodRepository:
    def __init__(self):
        self.foodStore = {}
        self.currentId = 0
        self._load()

    def Save(self, food):
        newId = self._nextId()
        self.foodStore[newId] = food
        food.id = newId
        self._persist()
        return food
    
    def Update(self, food_id, food):
        if food.id == None:
            return

        if food.id != food_id:
            return

        self.foodStore[food.id] = food
        self._persist()
        return self.foodStore[food_id]

    def GetAll(self):
        return self.foodStore.values()

    def GetBySearchTerm(self, search_term):
        return filter(lambda food: search_term in food.name, self.foodStore.values())

    def GetById(self, id):
        if not(id in self.foodStore):
            return Food(None, None, [])

        return self.foodStore[id]

    def Delete(self, id):
        if id in self.foodStore:
            del self.foodStore[id]
            self._persist()

    def _persist(self):
        filePath = path.join(Config.DATABASE_FOLDER, "foodStore.json")
        with open(filePath, "w") as f:
            foodList = list(map(lambda i: i.to_dict(), self.GetAll()))
            json.dump(foodList, f)

    def _load(self):
        filePath = path.join(Config.DATABASE_FOLDER, "foodStore.json")

        if (not(path.exists(filePath))):
            return

        with open(filePath, "r") as f:
            jsonArray = json.load(f)
            
        self.foodStore = dict((js['id'], Food.fromJson(js)) for js in jsonArray)
        self.currentId = max(self.foodStore.keys())

    def _nextId(self):
        self.currentId += 1
        return self.currentId
        


