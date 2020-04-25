#!flask/bin/python
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from cookbookServer import app
from cookbookServer.recipeCollectionService import RecipeCollectionService

recipeCollectionService = RecipeCollectionService()

@app.route('/api/recipeCollection', methods=['POST'])
def create_recipeCollection():
    if not request.json:
        abort(400)

    collection = recipeCollectionService.create(request.json)

    return jsonify(collection), 201

@app.route('/api/recipeCollection/<int:recipe_id>', methods=['PUT'])
def update_recipeCollection(collection_id):
    if not request.json:
        abort(400)

    collection = recipeCollectionService.update(collection_id, request.json)

    return jsonify(collection), 201

@app.route('/api/recipeCollection/', methods=['GET'])
def get_all_recipeCollections():
    return jsonify(recipeCollectionService.get_all())

@app.route('/api/recipeCollection/<int:recipe_id>', methods=['GET'])
def get_recipeCollections(collection_id):
    collection = recipeCollectionService.get_by_id(collection_id)
    if collection['id'] is None:
        abort(404)
    return jsonify(collection)

@app.route('/api/recipeCollection/<int:recipe_id>', methods=['DELETE'])
def delete_recipeCollection(collection_id):
    recipeCollectionService.delete(collection_id)
    return jsonify({'result': True})