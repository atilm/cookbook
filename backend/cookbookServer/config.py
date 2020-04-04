import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DATABASE_FOLDER = ""
    RECIPE_REPOSITORY = "recipeStore.json"