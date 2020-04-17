from cookbookServer.recipeRepository import RecipeRepository
from cookbookServer.recipe import Recipe
from cookbookServer.config import Config
import random

class RecipeService:
    def __init__(self):
        self.repository = RecipeRepository(Config())

    def create(self, jsonData):
        return self.repository.save(Recipe.from_dict(jsonData)).to_dict()

    def get_all(self):
        return self._to_json_list(self.repository.get_all())

    def get_by_id(self, id):
        return self.repository.get(id).to_dict()

    def get_by_search_term(self, search_term):
        return self._to_json_list(self.repository.get_by_search_term(search_term))

    def get_random(self, requestedNumber, tags):
        filteredItems = self.__recipesWithOneOfTags__(tags)
        items = [random.choice(filteredItems) for i in range(requestedNumber)]
        return self._to_json_list(items)

    def __recipesWithOneOfTags__(self, tags):
        allItems = list(self.repository.get_all())
        results = []

        if len(tags) == 0:
            return allItems

        for recipe in allItems:
            for tag in recipe.tags:
                if tag in tags:
                    results.append(recipe)
        
        return results

    def update(self, food_id, jsonData):
        return self.repository.update(Recipe.from_dict(jsonData)).to_dict()

    def delete(self, id):
        self.repository.delete(id)

    def _to_json_list(self, objectList):
        return list(map(lambda i: i.to_dict(), objectList))