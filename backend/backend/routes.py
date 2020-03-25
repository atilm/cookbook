#!flask/bin/python
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from backend import app
from backend.foodService import FoodService

foodService = FoodService()

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/api/food')
def get_all_food():
    return jsonify(foodService.get_all())

@app.route('/api/food/<int:food_id>', methods=['GET'])
def get_food(food_id):
    food = foodService.get_by_id(food_id)
    if food['id'] is None:
        abort(404)
    return jsonify(food)

@app.route('/api/food', methods=['POST'])
def create_food():
    if not request.json:
        abort(400)

    food = foodService.create(request.json)

    return jsonify(food), 201

@app.route('/api/food/<int:food_id>', methods=['DELETE'])
def delete_food(food_id):
    foodService.delete(food_id)
    return jsonify({'result': True})
    