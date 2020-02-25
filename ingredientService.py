from ingredient import *

class IngredientService:
    def __init__(self):
        self.ingredients = []
        self.ingredients.append(Ingredient("Carrot", 123))
        self.ingredients.append(Ingredient("Banana", 456))

    def get_all(self):
        return list(map(lambda i: i.to_dict(), self.ingredients))

    