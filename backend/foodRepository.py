from backend.food import Food
from backend.config import Config
from os import path
import json

class FoodRepository:
    def __init__(self):
        self.foodStore = {}
        self.currentId = 0

    def _nextId(self):
        self.currentId += 1
        return self.currentId

    def Save(self, food):
        newId = self._nextId()
        self.foodStore[newId] = food
        food.id = newId
    
    def Update(self, food):
        if food.id == None:
            return

        self.foodStore[food.id] = food

    def GetAll(self):
        return self.foodStore.values()

    def GetById(self, id):
        if not(id in self.foodStore):
            return Food("undefined food")

        return self.foodStore[id]

    def Delete(self, id):
        if id in self.foodStore:
            del self.foodStore[id]

    def _persist(self):
        filePath = "foodStore.json"
        with open(filePath, "w") as f:
            foodList = list(map(lambda i: i.to_dict(), self.GetAll()))
            json.dump(foodList, f)
        


