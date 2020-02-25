#!flask/bin/python
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from ingredientService import IngredientService

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

ingredients = IngredientService()

@app.route('/api/ingredients')
def get_ingredients():
    return jsonify(ingredients.get_all())

if __name__ == '__main__':
    app.run(debug=True)