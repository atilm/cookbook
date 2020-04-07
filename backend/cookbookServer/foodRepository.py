from cookbookServer.food import Food
from cookbookServer.recipe import Recipe
from cookbookServer.config import Config
from cookbookServer.database.storeManager import StoreManager
from os import path
import json

class FoodRepository:
    def __init__(self, config):
        self.config = config
        self.storeManager = StoreManager(self.config)
        self.foodStore = self.storeManager.instance.foodStore
        self.recipeStore = self.storeManager.instance.recipeStore

    def Save(self, food):
        foodWithId = self.foodStore.add(food.to_dict())

        return Food.from_dict(foodWithId)
    
    def Update(self, food):
        oldFood = self.GetById(food.id)
        updatedJson = self.foodStore.update(food.to_dict())
        updatedFood = Food.from_dict(updatedJson)

        if updatedFood.name != oldFood.name:
            self.__update_food_name_in_recipes(updatedFood)

        return updatedFood

    def GetAll(self):
        return self.__to_food_array(self.foodStore.get_all())

    def GetBySearchTerm(self, search_term):
        return filter(lambda food: search_term in food.name, self.GetAll())

    def GetById(self, id):
        return Food.from_dict(self.foodStore.get(id))

    def Delete(self, id):
        self.foodStore.remove(id)

    def __to_food_array(self, jsonArray):
        return [Food.from_dict(json) for json in jsonArray]

    def __to_recipe_array(self, jsonArray):
        return [Recipe.from_dict(json) for json in jsonArray]

    def __update_food_name_in_recipes(self, food):
        allRecipes = self.__to_recipe_array(self.recipeStore.get_all())

        for recipe in allRecipes:
            for ingredient in recipe.ingredients:
                if ingredient["food"]["id"] == food.id:
                    ingredient["food"]["name"] = food.name
        


