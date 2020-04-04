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
        recipe.ingredients = Recipe._updateIngredientsFormat(dict['ingredients'])
        recipe.instructions = dict['instructions']
        
        return recipe

    @classmethod
    def _updateIngredientsFormat(cls, jsonArray):
        newFormat = []
        for entry in jsonArray:
            if 'food_id' in entry:
                id = entry['food_id']
                name = entry['food_name']
                amount = entry['amount']
                unit = entry['unit']
                newFormat.append(Recipe.buildIngredient(id, name, amount, unit))
            else:
                newFormat.append(entry)
        return newFormat

    def to_dict(self):
        return { 
            'id' : self.id,
            'name' : self.name,
            'numberOfPeople' : self.numberOfPeople,
            'tags' : self.tags,
            'ingredients' : self.ingredients,
            'instructions' : self.instructions }