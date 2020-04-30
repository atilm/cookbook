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
        <div class="col"><button class="btn btn-sm" @click="saveList()">Save</button></div>
        <div v-if="lastSavedCollection"><p>Saved: {{lastSavedCollection.id}}</p></div>
      </div>
    </div>
</template>

<script>
import RecipeService from '../common/recipeService';
import RecipeCollection from '../common/recipeCollection';
import RecipeCollectionService from "../common/recipeCollectionService";

export default {
    name: 'random-recipes-view',
    data() {
        return {
            randomRecipeItems: [],
            lastSavedCollection: null
        }
    },
    mounted() {
        this.recipeService = new RecipeService();
        this.recipeCollectionService = new RecipeCollectionService();
        this.recipeService.getRandomlyChosen(7, ["Hauptgericht"])
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
            this.recipeService.getRandomlyChosen(1, ["Hauptgericht"])
                .then(recipes => vm.$set(vm.randomRecipeItems, index, recipes[0]));
        },
        saveList: function() {
            let collection = new RecipeCollection();
            collection.recipeIds = this.randomRecipeItems.map(item => item.id);

            let vm = this;
            this.recipeCollectionService.create(collection)
            .then(c => vm.lastSavedCollection = c);
        }
    }
}
</script>

<style>

</style>