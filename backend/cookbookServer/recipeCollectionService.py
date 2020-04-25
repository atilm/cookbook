from cookbookServer.config import Config
from cookbookServer.recipeCollectionRepository import RecipeCollectionRepository
from cookbookServer.recipeCollection import RecipeCollection

class RecipeCollectionService:
    def __init__(self):
        self.repository = RecipeCollectionRepository(Config())

    def create(self, jsonData):
        return self.repository.save(RecipeCollection.from_dict(jsonData)).to_dict()

    def get_all(self):
        return self.__to_json_list__(self.repository.get_all())

    def get_by_id(self, id):
        return self.repository.get_by_id(id).to_dict()

    def update(self, jsonData):
        return self.repository.update(RecipeCollection.from_dict(jsonData)).to_dict()

    def delete(self, id):
        self.repository.delete(id)

    def __to_json_list__(self, recipeCollections):
        return [rc.to_dict() for rc in recipeCollections]