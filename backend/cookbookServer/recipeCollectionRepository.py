from cookbookServer.database.storeManager import StoreManager
from cookbookServer.recipeCollection import RecipeCollection

class RecipeCollectionRepository:
    def __init__(self, config):
        self.config = config
        self.storeManager = StoreManager(self.config)
        self.store = self.storeManager.instance.recipeCollectionStore

    def save(self, recipeCollection):
        collectionWithId = self.store.add(recipeCollection.to_dict())

        return RecipeCollection.from_dict(collectionWithId)

    def get_all(self):
        return self.__to_collections__(self.store.get_all())

    def get_by_id(self, id):
        return RecipeCollection.from_dict(self.store.get(id))

    def update(self, recipeCollection):
        return RecipeCollection.from_dict(self.store.update(recipeCollection.to_dict()))

    def delete(self, recipeCollectionId):
        pass

    def __to_collections__(self, jsonArray):
        return [RecipeCollection.from_dict(json) for json in jsonArray]