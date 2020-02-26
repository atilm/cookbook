#!flask/bin/python
from flask import jsonify
from flask import abort
from backend import app
from backend.foodService import FoodService

foodService = FoodService()

@app.route('/api/food')
def get_all_food():
    return jsonify(foodService.get_all())

@app.route('/api/food/<int:food_id>', methods=['GET'])
def get_food(food_id):
    food = foodService.get_by_id(food_id)
    if food['id'] is None:
        abort(404)
    return jsonify(food)