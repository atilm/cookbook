from os import path
import json
from cookbookServer.config import Config
from cookbookServer.recipe import Recipe
from cookbookServer.indexedStore import IndexedStore

class RecipeRepository:
    def __init__(self, repositoryFileName):
        self.repositoryFileName = repositoryFileName
        self.recipeObjects = self._load()
        self.store = IndexedStore(self.recipeObjects)

    def save(self, recipe):
        if recipe.id != None:
            raise Exception("Object to save already has an id.")

        recipeWithId = self.store.add(recipe)
        self._persist()
        return recipeWithId

    def get_all(self):
        return self.store.get_all()

    def get(self, id):
        return self.store.get(id)

    def update(self, recipe):
        updatedRecipe = self.store.update(recipe)
        self._persist()
        return updatedRecipe

    def delete(self, recipeId):
        self.store.remove(recipeId)
        self._persist()

    def _persist(self):
        filePath = path.join(Config.DATABASE_FOLDER, self.repositoryFileName)
        with open(filePath, "w") as f:
            recipeList = self._to_json_list(self.store.get_all())
            json.dump(recipeList, f)

    def _load(self):
        filePath = path.join(Config.DATABASE_FOLDER, self.repositoryFileName)

        if (not(path.exists(filePath))):
            return []

        with open(filePath, "r") as f:
            jsonArray = json.load(f)

        return [Recipe.from_dict(js) for js in jsonArray]

    def _to_json_list(self, objectList):
        return list(map(lambda i: i.to_dict(), objectList))

