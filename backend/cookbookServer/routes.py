#!flask/bin/python
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from cookbookServer import app
from cookbookServer.foodService import FoodService
from cookbookServer.recipeService import RecipeService
from cookbookServer.tagService import TagService

foodService = FoodService()
recipeService = RecipeService()
tagService = TagService()

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# Food

@app.route('/api/food', methods=['GET'])
def get_all_food():
    if "searchTerm" in request.args:
        return jsonify(foodService.get_by_search_term(request.args["searchTerm"]))
    else:
        return jsonify(foodService.get_all())

@app.route('/api/food/<int:food_id>', methods=['GET'])
def get_food(food_id):
    food = foodService.get_by_id(food_id)
    if food['id'] is None:
        abort(404)
    return jsonify(food)

@app.route('/api/food/random', methods=['GET'])
def get_random():
    requestedNumber = 5

    if "number" in request.args:
        requestedNumber = int(request.args["number"])

    return jsonify(foodService.get_random(requestedNumber))

@app.route('/api/food', methods=['POST'])
def create_food():
    if not request.json:
        abort(400)

    food = foodService.create(request.json)

    return jsonify(food), 201

@app.route('/api/food/<int:food_id>', methods=['PUT'])
def update_food(food_id):
    if not request.json:
        abort(400)

    food = foodService.update(food_id, request.json)

    return jsonify(food), 201

@app.route('/api/food/<int:food_id>', methods=['DELETE'])
def delete_food(food_id):
    foodService.delete(food_id)
    return jsonify({'result': True})
    
# Recipe

@app.route('/api/recipe', methods=['POST'])
def create_recipe():
    if not request.json:
        abort(400)

    recipe = recipeService.create(request.json)

    return jsonify(recipe), 201

@app.route('/api/recipe/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    if not request.json:
        abort(400)

    recipe = recipeService.update(recipe_id, request.json)

    return jsonify(recipe), 201

@app.route('/api/recipe/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipeService.delete(recipe_id)
    return jsonify({'result': True})

@app.route('/api/recipe', methods=['GET'])
def get_all_recipes():
    return jsonify(recipeService.get_all())

@app.route('/api/recipe/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = recipeService.get_by_id(recipe_id)
    if recipe['id'] is None:
        abort(404)
    return jsonify(recipe)

# Tags
@app.route('/api/tag', methods=['GET'])
def get_all_tags():
    return jsonify(tagService.get_all())