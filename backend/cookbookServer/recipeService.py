from cookbookServer.recipeRepository import RecipeRepository
from cookbookServer.recipe import Recipe
from cookbookServer.config import Config

class RecipeService:
    def __init__(self):
        self.repository = RecipeRepository(Config.RECIPE_REPOSITORY)

    def create(self, jsonData):
        return self.repository.Save(Recipe.from_dict(jsonData)).to_dict()

    def get_all(self):
        return self._to_json_list(self.repository.get_all())

    def get_by_id(self, id):
        return self.repository.get(id).to_dict()

    def update(self, food_id, jsonData):
        return self.repository.update(Recipe.from_dict(jsonData)).to_dict()

    def delete(self, id):
        self.repository.delete(id)

    def _to_json_list(self, objectList):
        return list(map(lambda i: i.to_dict(), objectList))