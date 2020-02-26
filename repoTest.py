from backend.foodRepository import FoodRepository
from backend.food import Food

repo = FoodRepository()

repo.Save(Food("Banana", 456))
repo.Save(Food("Apple", 123))
repo.Save(Food("Carrot", 0.56))

repo._persist()