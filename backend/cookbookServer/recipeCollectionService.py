from cookbookServer.config import Config
from cookbookServer.recipeCollectionRepository import RecipeCollectionRepository
from cookbookServer.recipeCollection import RecipeCollection
from cookbookServer.recipeService import RecipeRepository
from cookbookServer.recipeLink import RecipeLink

class RecipeCollectionService:
    def __init__(self):
        self.repository = RecipeCollectionRepository(Config())
        self.recipeRepository = RecipeRepository(Config())

    def create(self, jsonData):
        return self.repository.save(RecipeCollection.from_dict(jsonData)).to_dict()

    def get_all(self):
        data = self.__to_dict_list__(self.repository.get_all())
        return [self.__add_recipe_links__(d) for d in data]

    def get_by_id(self, id):
        data = self.repository.get_by_id(id).to_dict()
        data = self.__add_recipe_links__(data)
        return data

    def update(self, jsonData):
        return self.repository.update(RecipeCollection.from_dict(jsonData)).to_dict()

    def delete(self, id):
        self.repository.delete(id)

    def __to_dict_list__(self, recipeCollections):
        return [rc.to_dict() for rc in recipeCollections]

    def __add_recipe_links__(self, recipe_collection_dict):
        recipes = self.recipeRepository.get_by_ids(recipe_collection_dict['recipeIds'])
        recipe_collection_dict['recipes'] = [RecipeLink(r).to_dict() for r in recipes]
        return recipe_collection_dict