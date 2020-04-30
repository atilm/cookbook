<template>
<div class="container">
    <div class="row">
        <div class="col">
            <h1>Recipes</h1>
            <form @submit.prevent="searchRecipes" class="form-inline mb-2">
                <div class="form-group">
                    <input type="text" class="form-control" v-model="searchTerm"/>
                </div>
                <div class="form-group">
                    <Button type="submit" class="btn btn-primary ml-2">Search</Button>
                </div>
            </form>
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
            recipeItems: [],
            searchTerm: ""
        }
    },
    mounted() {
        this.service = new RecipeService();
        this.updateList();
    },
    methods: {
        updateList: function() {
            let vm = this;
            this.service.get_all().then(items => vm.recipeItems = items );
        },
        searchRecipes: function() {
            let vm = this;
            this.service.get_by_search_term(vm.searchTerm)
                .then(items => vm.recipeItems = items);
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