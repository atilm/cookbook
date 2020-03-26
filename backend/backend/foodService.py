from backend.foodRepository import FoodRepository
from backend.food import Food

class FoodService:
    def __init__(self):
        self.repository = FoodRepository()

    def create(self, jsonData):
        return self.repository.Save(Food.fromJson(jsonData)).to_dict()

    def get_all(self):
        return list(map(lambda i: i.to_dict(), self.repository.GetAll()))

    def get_by_id(self, id):
        return self.repository.GetById(id).to_dict()

    def update(self, food_id, jsonData):
        return self.repository.Update(food_id, Food.fromJson(jsonData)).to_dict()

    def delete(self, id):
        self.repository.Delete(id)

    