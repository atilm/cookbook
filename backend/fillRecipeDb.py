from cookbookServer.recipe import Recipe
from cookbookServer.recipeRepository import RecipeRepository

recipeA = Recipe()
recipeA.name = "Reisfladen"
recipeA.tags = ["Kuchen", "belgisch", "vegetarisch"]

recipeB = Recipe()
recipeB.name = "Lasagne"
recipeB.tags = ["Hauptgericht", "italienisch"]

repo = RecipeRepository("recipeStore.json")
repo.save(recipeA)
repo.save(recipeB)
