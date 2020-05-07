<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <h1>{{currentRecipe.name}}</h1>
                <router-link :to="{ name: 'editRecipe', params: { id: currentRecipe.id }}" tag="button" class="btn btn-primary btn-sm mb-2">Edit</router-link>
                <form @submit.prevent="rescaleRecipe" class="form-inline mb-2">
                    <label for="numberOfPersons">Personen: </label>
                    <input type="number" class="form-control ml-2" id="numberOfPersons" v-model="currentNumberOfPersons">
                    <button type="submit" class="btn btn-sm btn-primary ml-2">Rescale</button>
                </form>
                <table class="table table-striped">
                    <tbody>
                        <tr  v-for="(ingredient, index) in currentRecipe.ingredients" :key="index">
                            <td>{{ingredient.amount}} {{ingredient.unit}} </td>
                            <td>{{ingredient.food.name}}</td>
                        </tr>
                    </tbody>
                </table>
                <span v-html="currentInstructions"></span>
            </div>
        </div>
    </div>
</template>

<script>
import RecipeService from "../common/recipeService";
import Recipe from "../common/recipe";
import showdown from 'showdown';

export default {
    name: "recipe-details-view",
    data() {
        return {
            currentRecipe: new Recipe(),
            currentNumberOfPersons: null,
            currentInstructions: ""
        }
    },
    mounted() {
        this.service = new RecipeService();
        this.loadRecipe(this.$route.params.id);
    },
    methods: {
        loadRecipe: function(id){
            let vm = this;
            this.service.get(id).then(recipe => vm.parseRecipe(recipe));
        },
        parseRecipe: function(recipe){
            let vm = this;
            let markdownConverter = new showdown.Converter();

            vm.currentRecipe = recipe;
            vm.currentNumberOfPersons = recipe.numberOfPeople;
            vm.currentInstructions = markdownConverter.makeHtml(recipe.instructions);
        },
        rescaleRecipe: function(){
            let vm = this;
            this.service.get_scaled(vm.currentRecipe.id, vm.currentNumberOfPersons)
                .then(recipe => vm.parseRecipe(recipe));
        }
    }
}
</script>

<style scoped>

</style>