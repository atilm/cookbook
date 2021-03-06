from cookbookServer.database.indexedStore import IndexedStore

class StoreManager:
    class __StoreManager:
        def __init__(self, config):
            self.config = config
            self.foodStore = IndexedStore(self.config.FOOD_REPOSITORY)
            self.recipeStore = IndexedStore(self.config.RECIPE_REPOSITORY)
            self.recipeCollectionStore = IndexedStore(self.config.RECIPE_COLLECTION_REPOSITORY)

    instance = None

    def __init__(self, config):
        if not StoreManager.instance:
            StoreManager.instance = StoreManager.__StoreManager(config)

    def setConfig(self, config):
        StoreManager.instance = StoreManager.__StoreManager(config)