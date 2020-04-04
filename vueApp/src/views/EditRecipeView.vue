<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <form @submit.prevent="saveChanges">
                <legend>Edit Recipe</legend>
                <div class="form-group">
                    <label for="recipeName">Name</label>
                    <input type="text" class="form-control" id="recipeName" v-model="currentRecipe.name" />
                </div>
                <div class="form-group">
                    <label for="persons">Anzahl Personen</label>
                    <input type="number" class="form-control" id="persons" v-model="currentRecipe.numberOfPeople" />
                </div>
                <label for="ingredientForm">Zutaten</label>
                <div class="form-inline" id="ingredientForm" v-for="ingredient in currentRecipe.ingredients" :key="ingredient.food_id">
                    <input type="number" class="form-control" v-model="ingredient.amount" />
                    <vue-select :options="availableUnits" v-model="ingredient.unit" />
                    <vue-select :options="availableFood" label="name" v-model="ingredient.food" />
                </div>
                <button @click="addIngredient" class="btn btn-secondary btn-sm">Add</button>
                <div class="form-group">
                    <label for="instructions">Zubereitung</label>
                    <textarea class="form-control" id="instructions" v-model="currentRecipe.instructions" />
                </div>
                <button type="submit" class="btn btn-primary">Save</button>
            </form>
            </div>
        </div>
    </div>
</template>

<script>
import RecipeService from "../common/recipeService";
import FoodService from "../common/foodService";
import Recipe from "../common/recipe";

export default {
    name: 'edit-recipe-view',
    data() {
        return {
            currentRecipe: new Recipe(),
            availableUnits: ["g", "ml", "El", "Tl", "Stück"],
            availableFood: []
        }
    },
    mounted() {
        this.service = new RecipeService();
        this.loadRecipe(this.$route.params.id);

        this.foodService = new FoodService();
        this.loadAvailableFood();
    },
    methods: {
        loadRecipe: function(id) {
            let vm = this;
            this.service.get(id).then(recipe => this.currentRecipe = recipe);
        },
        loadAvailableFood: function() {
            let vm = this;
            this.foodService.get_all_names().then(foodList => this.availableFood = foodList);
        },
        addIngredient: function() {
            this.currentRecipe.ingredients.push(
                {
                    food: null,
                    amount: null,
                    unit: ""
                }
            );
        },
        saveChanges: function() {

        }
    }
}
</script>

<style scoped>

</style>