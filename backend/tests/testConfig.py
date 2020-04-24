import os
basedir = os.path.abspath(os.path.dirname(__file__))

class TestConfig(object):
    DATABASE_FOLDER = "testData"
    RECIPE_REPOSITORY = os.path.join(DATABASE_FOLDER, "testRecipeStore.json")
    RECIPE_COLLECTION_REPOSITORY = os.path.join(DATABASE_FOLDER, "testRecipeCollectionStore.json")
    FOOD_REPOSITORY = os.path.join(DATABASE_FOLDER, "testFoodStore.json")