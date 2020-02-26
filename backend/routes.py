#!flask/bin/python
from flask import jsonify
from backend import app
from backend.foodService import FoodService

foodService = FoodService()

@app.route('/api/food')
def get_food():
    return jsonify(foodService.get_all())