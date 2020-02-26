from ingredient import Ingredient

class IngredientRepository:
    def __init__(self):
        self.ingredients = {}
        self.currentId = 0

    def nextId(self):
        self.currentId += 1
        return self.currentId

    def Save(self, ingredient):
        self.ingredients[self.nextId()] = ingredient
        ingredient.id = 
    
    def Update(self, ingredient):
        if ingredient.id == None:
            return

        self.ingredients[ingredient.id] = ingredient

    def GetById(self, id):
        if not(id in self.ingredients):
            return Ingredient("undefined food")

        return self.ingredients[id]

    def Delete(self, id):
        if id in self.ingredients:
            del self.ingredients[id]
        
