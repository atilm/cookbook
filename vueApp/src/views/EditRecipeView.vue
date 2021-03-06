<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <div v-if="lastSaved.id" class="alert alert-primary mb-2" role="alert">
                    Saved recipe {{lastSaved.name}}.
                    <button type="button" class="close" @click="dismissNotification" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <form @submit.prevent="saveChanges" v-on:keydown.ctrl.s.prevent="saveChanges">
                <legend>Edit Recipe</legend>
                <div class="form-group">
                    <label for="recipeName">Name</label>
                    <input type="text" class="form-control" id="recipeName" ref="recipeNameInput" v-model="currentRecipe.name" />
                </div>
                <div class="form-group">
                    <label for="tagsSelect">Tags</label>
                    <vue-select multiple taggable push-tags :options="availableTags" v-model="currentRecipe.tags" />
                </div>
                <div class="form-group">
                    <label for="persons">Anzahl Personen</label>
                    <input type="number" class="form-control" id="persons" v-model="currentRecipe.numberOfPeople" />
                </div>
                <label for="ingredientForm">Zutaten</label>
                <button type="button" @click="loadAvailableFood" class="btn btn-secondary btn-sm">Update food list</button>
                <div class="form-inline mb-2" id="ingredientForm" v-for="(ingredient, index) in currentRecipe.ingredients" :key="ingredient.food_id">
                    <input v-focus type="number" step=".01" class="form-control amount-input mt-1" v-model="ingredient.amount" />
                    <vue-select class="ml-2" :options="availableUnits" v-model="ingredient.unit" />
                    <vue-select class="ml-2" :options="availableFood" label="name" v-model="ingredient.food" />
                    <button  type="button" class="btn btn-secondary btn-sm ml-1" @click="removeIngredient(index)">Remove</button>
                </div>
                <button  type="button" @click="addIngredient" class="btn btn-secondary btn-sm">Add</button>
                <div class="form-group">
                    <label for="instructions">Zubereitung</label>
                    <textarea class="form-control instructions-input" id="instructions" v-model="currentRecipe.instructions" />
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
import TagService from "../common/tagService";
import Recipe from "../common/recipe";

export default {
    name: 'edit-recipe-view',
    data() {
        return {
            currentRecipe: new Recipe(),
            lastSaved: new Recipe(),
            availableTags: [],
            availableUnits: ["g", "ml", "El", "Tl", "Stück", "Prise"],
            availableFood: []
        }
    },
    mounted() {
        this.service = new RecipeService();
        if ("id" in this.$route.params)
            this.loadRecipe(this.$route.params.id);

        this.foodService = new FoodService();
        this.loadAvailableFood();

        this.tagService = new TagService();
        this.loadAvailableTags();
    },
    directives: {
        focus: {
            inserted: function (el) {
                el.focus()
            }
        }
    },
    methods: {
        loadRecipe: function(id) {
            let vm = this;
            
            if (id === null) {
                this.currentRecipe = new Recipe();
                this.addIngredient();
            }
            else
                this.service.get(id).then(recipe => this.currentRecipe = recipe);
        },
        loadAvailableTags: function() {
            let vm = this;
            this.tagService.get_all().then(tags => vm.availableTags = tags);
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
        removeIngredient: function(index) {
            this.currentRecipe.ingredients.splice(index, 1);
        },
        saveChanges: function() {
            if (this.currentRecipe.id === null) {
                this.service.create(this.currentRecipe).then(recipe => {
                    this.lastSaved = recipe;
                    this.currentRecipe = new Recipe();
                });
            }
            else
                this.service.update(this.currentRecipe).then(recipe => this.lastSaved = recipe);
        },
        dismissNotification: function() {
            this.lastSaved = new Recipe();
        }
    }
}
</script>

<style scoped>
    .amount-input {
        width: 100px;
    }

    .instructions-input {
        height: 250px;
    }
</style>