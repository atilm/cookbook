from backend.foodRepository import FoodRepository

class FoodService:
    def __init__(self):
        self.repository = FoodRepository()

    def get_all(self):
        return list(map(lambda i: i.to_dict(), self.repository.GetAll()))

    