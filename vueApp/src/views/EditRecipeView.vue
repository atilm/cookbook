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
                    <input type="text" class="form-control" v-model="ingredient.unit" />
                    <input type="text" class="form-control" v-model="ingredient.food_name" />
                </div>
                <button @click="addIngredient" class="btn btn-secondary btn-sm">Add</button>
                <div class="form-group">
                    <label for="instructions">Zubereitung</label>
                    <input type="text" class="form-control" id="instructions" v-model="currentRecipe.instructions" />
                </div>
                <button type="submit" class="btn btn-primary">Save</button>
            </form>
            </div>
        </div>
    </div>
</template>

<script>
import RecipeService from "../common/recipeService";
import Recipe from "../common/recipe";

export default {
    name: 'edit-recipe-view',
    data() {
        return {
            currentRecipe: new Recipe()
        }
    },
    mounted() {
        this.service = new RecipeService();
        this.loadRecipe(this.$route.params.id);
    },
    methods: {
        loadRecipe: function(id) {
            let vm = this;
            this.service.get(id).then(recipe => this.currentRecipe = recipe);
        },
        addIngredient: function() {
            this.currentRecipe.ingredients.push(
                {
                    food_id: null,
                    food_name: "",
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