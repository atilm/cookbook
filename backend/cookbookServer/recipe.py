import copy

class Recipe:
    def __init__(self):
        self.id = None
        self.name = ""
        self.numberOfPeople = None
        self.tags = []
        self.ingredients = []
        self.instructions = ""

    def add_ingredient(self, food_id, food_name, amount, unit):
        self.ingredients.append(Recipe.buildIngredient(food_id, food_name, amount, unit))

    @classmethod
    def buildIngredient(cls, food_id, food_name, amount, unit):
        return {
            "food": {
                "id": food_id,
                "name": food_name
            },
            "amount": amount,
            "unit": unit}

    @classmethod
    def from_dict(cls, dict):
        recipe = cls()

        recipe.id = dict['id']
        recipe.name = dict['name']
        recipe.numberOfPeople = dict['numberOfPeople']
        recipe.tags = dict['tags']
        recipe.ingredients = dict['ingredients']
        recipe.instructions = dict['instructions']
        
        return recipe

    def to_dict(self):
        return { 
            'id' : self.id,
            'name' : self.name,
            'numberOfPeople' : self.numberOfPeople,
            'tags' : self.tags,
            'ingredients' : self.ingredients,
            'instructions' : self.instructions }

    def get_scaled(self, number_of_people):
        scaled_recipe = copy.deepcopy(self)

        if number_of_people == self.numberOfPeople:
            return scaled_recipe

        if self.numberOfPeople == None or self.numberOfPeople <= 0:
            raise Exception("Tried to scale recipe with undefined number of people.")

        for ingredient in scaled_recipe.ingredients:
            ingredient["amount"] = float(ingredient["amount"]) / self.numberOfPeople * number_of_people
        
        return scaled_recipe