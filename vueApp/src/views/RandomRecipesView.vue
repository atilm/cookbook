<template>
    <div class="container">
      <div class="row">
        <div class="col">
          <p>Seven randomly choosen recipes:</p>
          <table class="table">
                <tbody>
                    <tr  v-for="(recipe, index) in randomRecipeItems" :key="index">
                        <td><router-link :to="{ name: 'recipeDetails', params: { id: recipe.id }}">{{recipe.name}}</router-link></td>
                        <td>{{getTagsString(recipe)}}</td>
                        <td><button class="btn btn-secondary btn-sm" @click="otherRecipe(index)">Other</button></td>
                    </tr>
                </tbody>
            </table>
        </div>
      </div>
    </div>
</template>

<script>
import FoodService from "../common/recipeService"
import RecipeService from '../common/recipeService';

export default {
    name: 'random-recipes-view',
    data() {
        return {
            randomRecipeItems: []
        }
    },
    mounted() {
        this.recipeService = new RecipeService();
        this.recipeService.getRandomlyChosen(7)
            .then(recipeItems => this.randomRecipeItems = recipeItems);
    },
    methods: {
        getTagsString: function(recipe) {
            let resultString = "";
            
            for (let i = 0; i < recipe.tags.length; i++){
                resultString += recipe.tags[i];

                if (i < recipe.tags.length - 1)
                    resultString += " ";
            }

            return resultString;
        },
        otherRecipe: function(index){
            let vm = this;
            this.recipeService.getRandomlyChosen(1)
                .then(recipes => vm.$set(vm.randomRecipeItems, index, recipes[0]));
        }
    }
}
</script>

<style>

</style>