class RecipeLink:
    def __init__(self, recipe):
        self.recipe_id = recipe.id
        self.recipe_name = recipe.name

    def to_dict(self):
        return {
            'id' : self.recipe_id,
            'name' : self.recipe_name
        }
    