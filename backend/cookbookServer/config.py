import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    USE_CORS = True
    DATABASE_FOLDER = "C:/Projects/Data/Cookbook"
    RECIPE_REPOSITORY = os.path.join(DATABASE_FOLDER, "recipeStore.json")
    RECIPE_COLLECTION_REPOSITORY = os.path.join(DATABASE_FOLDER, "recipeCollectionStore.json")
    FOOD_REPOSITORY = os.path.join(DATABASE_FOLDER, "foodStore.json")