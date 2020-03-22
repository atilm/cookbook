from backend.foodRepository import FoodRepository
from backend.food import Food

class FoodService:
    def __init__(self):
        self.repository = FoodRepository()

    def get_all(self):
        return list(map(lambda i: i.to_dict(), self.repository.GetAll()))

    def get_by_id(self, id):
        return self.repository.GetById(id).to_dict()

    def create(self, jsonData):
        return self.repository.Save(Food.fromJson(jsonData)).to_dict()

    