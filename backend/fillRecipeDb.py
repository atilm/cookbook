from cookbookServer.recipe import Recipe
from cookbookServer.recipeRepository import RecipeRepository

recipeA = Recipe()
recipeA.name = "Reisfladen"
recipeA.tags = ["Kuchen", "belgisch", "vegetarisch"]

recipeB = Recipe()
recipeB.name = "Lasagne"
recipeB.numberOfPeople = 4
recipeB.add_ingredient(None, "Lasagneblätter", 500, "g")
recipeB.add_ingredient(None, "Hackfleischsoße", 1000, "ml")
recipeB.add_ingredient(None, "Bechamelsoße", 500, "ml")
recipeB.add_ingredient(None, "Käse", 200, "g")
recipeB.tags = ["Hauptgericht", "italienisch"]
recipeB.instructions = "Alles einschichten. Dann die Lasagne bei 200 °C eine viertel bis halbe Stunde backen. Den Parmesankäse erst 10 min vor Schluss auf die Lasagne geben und mit Olivenöl betreufeln."

repo = RecipeRepository("recipeStore.json")
repo.save(recipeA)
repo.save(recipeB)
