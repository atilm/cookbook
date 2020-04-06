from os import path
from cookbookServer.recipe import Recipe
from cookbookServer.storeManager import StoreManager
from cookbookServer.indexedStore import IndexedStore

class RecipeRepository:
    def __init__(self, config):
        self.config = config
        self.storeManager = StoreManager(self.config)
        self.recipeStore = self.storeManager.instance.recipeStore

    def save(self, recipe):
        if recipe.id != None:
            raise Exception("Object to save already has an id.")

        recipeWithId = self.recipeStore.add(recipe.to_dict())

        return Recipe.from_dict(recipeWithId)

    def get_all(self):
        return self.__to_Recipes(self.recipeStore.get_all())

    def get(self, id):
        return Recipe.from_dict(self.recipeStore.get(id))

    def update(self, recipe):
        updatedRecipe = self.recipeStore.update(recipe.to_dict())

        return Recipe.from_dict(updatedRecipe)

    def delete(self, recipeId):
        self.recipeStore.remove(recipeId)

    def __to_Recipes(self, jsonArray):
        return [Recipe.from_dict(json) for json in jsonArray]

