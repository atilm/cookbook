<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <h1>{{currentRecipe.name}}</h1>
                <router-link :to="{ name: 'editRecipe', params: { id: currentRecipe.id }}" tag="button" class="btn btn-primary btn-sm">Edit</router-link>
                <p>Für {{currentRecipe.numberOfPeople}} Personen</p>
                <table class="table table-striped">
                    <tbody>
                        <tr  v-for="(ingredient, index) in currentRecipe.ingredients" :key="index">
                            <td>{{ingredient.amount}} {{ingredient.unit}} </td>
                            <td>{{ingredient.food.name}}</td>
                        </tr>
                    </tbody>
                </table>
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