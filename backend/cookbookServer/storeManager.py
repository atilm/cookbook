from cookbookServer.indexedStore import IndexedStore

class StoreManager:
    class __StoreManager:
        def __init__(self, config):
            self.config = config
            print("Store manager setting up: " + self.config.FOOD_REPOSITORY)
            self.foodStore = IndexedStore(self.config.FOOD_REPOSITORY)
            self.recipeStore = IndexedStore(self.config.RECIPE_REPOSITORY)

    instance = None

    def __init__(self, config):
        if not StoreManager.instance:
            StoreManager.instance = StoreManager.__StoreManager(config)

    def setConfig(self, config):
        StoreManager.instance = StoreManager.__StoreManager(config)