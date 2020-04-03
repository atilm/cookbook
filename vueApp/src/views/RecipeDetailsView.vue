<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <h1>{{currentRecipe.name}}</h1>
                <p>Für {{currentRecipe.numberOfPeople}} Personen</p>
                <ul>
                    <li v-for="ingredient in currentRecipe.ingredients" :key="ingredient.food_id">
                        {{ingredient.amount}} {{ingredient.unit}} {{ingredient.food_name}}
                    </li>
                </ul>
                <p>{{currentRecipe.instructions}}</p>
            </div>
        </div>
    </div>
</template>

<script>
import RecipeService from "../common/recipeService"
import Recipe from "../common/recipe"

export default {
    name: "recipe-details-view",
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
        loadRecipe: function(id){
            let vm = this;
            this.service.get(id).then(recipe => vm.currentRecipe = recipe);
        }
    }
}
</script>

<style scoped>

</style>