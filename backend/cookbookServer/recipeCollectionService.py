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
        newCollection = self.__collection_from_json__(jsonData)
        returnCollection = self.repository.save(newCollection)
        return self.__json_from_collection__(returnCollection)

    def get_all(self):
        data = self.__to_dict_list__(self.repository.get_all())
        return [self.__recipeIds_to_links__(d) for d in data]

    def get_by_id(self, id):
        collection = self.repository.get_by_id(id)
        return self.__json_from_collection__(collection)

    def update(self, jsonData):
        newCollection = self.__collection_from_json__(jsonData)
        returnCollection = self.repository.update(newCollection)
        return self.__json_from_collection__(returnCollection)

    def delete(self, id):
        self.repository.delete(id)

    def __to_dict_list__(self, recipeCollections):
        return [rc.to_dict() for rc in recipeCollections]

    def __collection_from_json__(self, jsonData):
        convertedJson = self.__recipeLinks_to_ids__(jsonData)
        return RecipeCollection.from_dict(convertedJson)

    def __json_from_collection__(self, collection):
        dictData = collection.to_dict()
        return self.__recipeIds_to_links__(dictData)

    def __recipeIds_to_links__(self, recipe_collection_dict):
        recipes = self.recipeRepository.get_by_ids(recipe_collection_dict['recipeIds'])
        recipe_collection_dict['recipes'] = [RecipeLink(r).to_dict() for r in recipes]
        del recipe_collection_dict['recipeIds']
        return recipe_collection_dict

    def __recipeLinks_to_ids__(self, recipe_collection_dict):
        links = recipe_collection_dict['recipes']
        recipe_collection_dict['recipeIds'] = [link['id'] for link in links]
        del recipe_collection_dict['recipes']
        return recipe_collection_dict