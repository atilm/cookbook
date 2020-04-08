<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <form @submit.prevent="saveChanges">
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
                <button @click="loadAvailableFood" class="btn btn-secondary btn-sm">Update food list</button>
                <div class="form-inline" id="ingredientForm" v-for="(ingredient, index) in currentRecipe.ingredients" :key="ingredient.food_id">
                    <input v-focus type="number" class="form-control amount-input" v-model="ingredient.amount" />
                    <vue-select :options="availableUnits" v-model="ingredient.unit" />
                    <vue-select :options="availableFood" label="name" v-model="ingredient.food" />
                    <button class="btn btn-secondary btn-sm" @click="removeIngredient(index)">Remove</button>
                </div>
                <button @click="addIngredient" class="btn btn-secondary btn-sm">Add</button>
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
            availableTags: [],
            availableUnits: ["g", "ml", "El", "Tl", "Stück", "Prise"],
            availableFood: []
        }
    },
    mounted() {
        this.service = new RecipeService();
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
            if (this.currentRecipe.id === null)
                this.service.create(this.currentRecipe);
            else
                this.service.update(this.currentRecipe);
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