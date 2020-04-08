<template>
<div class="container">
    <div class="row">
        <div class="col">
            <h1>Recipes</h1>
            <table class="table">
                <tbody>
                    <tr  v-for="(recipe) in recipeItems" :key="recipe.id">
                        <td><router-link :to="{ name: 'recipeDetails', params: { id: recipe.id }}">{{recipe.name}}</router-link></td>
                        <td>{{getTagsString(recipe)}}</td>
                        <td><button class="btn btn-secondary btn-sm" @click="deleteRecipe(recipe.id)">Delete</button></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
</template>

<script>
import RecipeService from "../common/recipeService";

export default {
    name: 'list-recipes-view',
    data() {
        return {
            recipeItems: []
        }
    },
    mounted() {
        this.service = new RecipeService();
        this.updateList();
    },
    methods: {
        updateList: function() {
            let vm = this;
            this.service.get_all().then(items => this.recipeItems = items );
        },
        getTagsString: function(recipe) {
            let resultString = "";
            
            for (let i = 0; i < recipe.tags.length; i++){
                resultString += recipe.tags[i];

                if (i < recipe.tags.length - 1)
                    resultString += " ";
            }

            return resultString;
        },
        deleteRecipe: function(id) {
            this.service.delete(id);
            this.updateList();
        }
    }
}
</script>

<style>

</style>