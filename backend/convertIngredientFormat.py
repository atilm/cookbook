from cookbookServer.recipeRepository import RecipeRepository

repo = RecipeRepository("recipeStore.json")

repo._load()

repo._persist()