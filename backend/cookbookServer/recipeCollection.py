from datetime import datetime, date

class RecipeCollection:
    def __init__(self):
        self.id = None
        self.date = date.today()
        self.recipeIds = []

    def to_dict(self):
        return {
            'id' : self.id,
            'date' : self.date.isoformat(),
            'recipes' : self.recipeIds
        }

    @classmethod
    def from_dict(cls, dict):
        recipeCollection = cls()
        recipeCollection.id = dict['id']
        recipeCollection.date = datetime.strptime(dict['date'], "%Y-%m-%d").date()
        recipeCollection.recipeIds = dict['recipes']

        return recipeCollection
