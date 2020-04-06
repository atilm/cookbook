from cookbookServer.recipeRepository import RecipeRepository
from cookbookServer.config import Config

class TagService:
    def __init__(self):
        self.recipeRepository = RecipeRepository(Config())

    def get_all(self):
        setOfTags = set()
        allRecipes = self.recipeRepository.get_all()
        for recipe in allRecipes:
            for tag in recipe.tags:
                setOfTags.add(tag)

        return list(setOfTags)