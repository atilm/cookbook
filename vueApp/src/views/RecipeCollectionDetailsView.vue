<template>
<div class="container">
    <div class="row">
        <div class="col">
            <h1>Recipe collection from {{recipeCollection.date}}</h1>
            <table class="table">
                <tr v-for="(recipeLink, index) in recipeCollection.recipes" :key="index">
                    <td><router-link :to="{ name: 'recipeDetails', params: { id: recipeLink.id }}">{{recipeLink.name}}</router-link></td>
                    <td><button class="btn btn-secondary btn-sm" @click="removeLink(index)">Remove</button></td>
                </tr>
            </table>
        </div>
    </div>
</div>
</template>

<script>
import RecipeCollection from '../common/recipeCollection';
import RecipeCollectionService from '../common/recipeCollectionService';

export default {
    name: "recipe-collections-details-view",
    data() {
        return {
            recipeCollection : new RecipeCollection() 
        }
    },
    mounted() {
        this.service = new RecipeCollectionService();
        this.loadCollection(this.$route.params.id)
    },
    methods: {
        loadCollection: function(id) {
            let vm = this;
            this.service.get(id).then(c => vm.recipeCollection = c);
        },
        removeLink: function(index) {
            this.recipeCollection.recipes.splice(index, 1);
            let vm = this;
            this.service.update(this.recipeCollection).then(c => this.recipeCollection = c);
        }
    }
}
</script>

<style scoped>

</style>