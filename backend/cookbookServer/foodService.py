from cookbookServer.foodRepository import FoodRepository
from cookbookServer.food import Food
from cookbookServer.config import Config
import random

class FoodService:
    def __init__(self):
        self.repository = FoodRepository(Config())

    def create(self, jsonData):
        return self.repository.Save(Food.fromJson(jsonData)).to_dict()

    def get_all(self):
        return list(map(lambda i: i.to_dict(), self.repository.GetAll()))

    def get_by_search_term(self, search_term):
        return list(map(lambda i: i.to_dict(), self.repository.GetBySearchTerm(search_term)))

    def get_by_id(self, id):
        return self.repository.GetById(id).to_dict()

    def get_random(self, requestedNumber):
        allItems = list(self.repository.GetAll())
        items = [random.choice(allItems) for i in range(requestedNumber)]
        return list(map(lambda i: i.to_dict(), items))

    def update(self, food_id, jsonData):
        return self.repository.Update(Food.fromJson(jsonData)).to_dict()

    def delete(self, id):
        self.repository.Delete(id)
