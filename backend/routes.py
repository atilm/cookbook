#!flask/bin/python
from flask import jsonify
from backend import app
from backend.ingredientService import IngredientService

ingredients = IngredientService()

@app.route('/api/ingredients')
def get_ingredients():
    return jsonify(ingredients.get_all())