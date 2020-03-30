class Recipe:
    def __init__(self):
        self.id = None
        self.name = ""
        self.tags = []
        self.ingredients = []
        self.instructions = ""

    def add_ingredient(self, food_id, food_name, amount, unit):
        self.ingredients.append({ 
            "food_id": food_id,
            "food_name": food_name,
            "amount": amount,
            "unit": unit})

    @classmethod
    def from_dict(cls, dict):
        recipe = cls()

        recipe.id = dict['id']
        recipe.name = dict['name']
        recipe.tags = dict['tags']
        recipe.ingredients = dict['ingredients']
        recipe.instructions = dict['instructions']
        
        return recipe

    def to_dict(self):
        return { 
            'id' : self.id,
            'name' : self.name,
            'tags' : self.tags,
            'ingredients' : self.ingredients,
            'instructions' : self.instructions }