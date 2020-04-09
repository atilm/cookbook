from os import path
from cookbookServer.recipe import Recipe
from cookbookServer.database.storeManager import StoreManager

class RecipeRepository:
    def __init__(self, config):
        self.config = config
        self.storeManager = StoreManager(self.config)
        self.recipeStore = self.storeManager.instance.recipeStore

    def save(self, recipe):
        recipeWithId = self.recipeStore.add(recipe.to_dict())

        return Recipe.from_dict(recipeWithId)

    def get_all(self):
        return self.__to_Recipes(self.recipeStore.get_all())

    def get(self, id):
        return Recipe.from_dict(self.recipeStore.get(id))

    def get_by_search_term(self, search_term):
        return list(filter(lambda r: self.__has_search_term(r, search_term), self.get_all()))

    def update(self, recipe):
        updatedRecipe = self.recipeStore.update(recipe.to_dict())

        return Recipe.from_dict(updatedRecipe)

    def delete(self, recipeId):
        self.recipeStore.remove(recipeId)

    def __has_search_term(self, recipe, search_term):
        lower_term = search_term.lower()

        if lower_term in recipe.name.lower():
            return True

        for ingredient in recipe.ingredients:
            if ingredient["food"] != None and lower_term in ingredient["food"]["name"].lower():
                return True

    def __to_Recipes(self, jsonArray):
        return [Recipe.from_dict(json) for json in jsonArray]

