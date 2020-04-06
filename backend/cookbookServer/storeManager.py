from cookbookServer.indexedStore import IndexedStore

class StoreManager:
    class __StoreManager:
        def __init__(self, config):
            self.config = config
            self.foodStore = IndexedStore(config.FOOD_REPOSITORY)
            self.recipeStore = IndexedStore(config.RECIPE_REPOSITORY)

    instance = None

    def __init__(self, config):
        if not StoreManager.instance:
            StoreManager.instance = StoreManager.__StoreManager(config)