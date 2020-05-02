#!flask/bin/python
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from cookbookServer import app
from cookbookServer.recipeService import RecipeService

recipeService = RecipeService()

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
    if "searchTerm" in request.args:
        return jsonify(recipeService.get_by_search_term(request.args["searchTerm"]))
    else:
        return jsonify(recipeService.get_all())

@app.route('/api/recipe/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    if "numberOfPeople" in request.args:
        recipe = recipeService.get_scaled_by_id(recipe_id, request.args["numberOfPeople"])
    else:
        recipe = recipeService.get_by_id(recipe_id)

    if recipe['id'] is None:
        abort(404)
    return jsonify(recipe)

@app.route('/api/recipe/random', methods=['GET'])
def get_random_recipes():
    requestedNumber = 1
    tags = []

    if "number" in request.args:
        requestedNumber = int(request.args["number"])

    if "tags" in request.args:
        tags = list(map(lambda s: s.strip(), request.args["tags"].split(',')))

    return jsonify(recipeService.get_random(requestedNumber, tags))