<template>
<div class="container">
    <div class="row">
        <div class="col">
            <table class="table">
                <tbody>
                    <tr v-for="collection in recipeCollections" :key="collection.id">
                        <td><router-link :to="{ name: 'recipeCollectionDetails', params: { id: collection.id }}">{{collection.date}}</router-link></td>
                        <td>{{previewString(collection)}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
</template>

<script>
import RecipeCollectionService from "../common/recipeCollectionService";

export default {
    name: "list-recipe-collections-view",
    data() {
        return {
            recipeCollections: []
        }
    },
    mounted() {
        this.service = new RecipeCollectionService();
        this.updateList();
    },
    methods: {
        updateList: function() {
            let vm = this;
            this.service.get_all()
            .then(collections => vm.recipeCollections = collections);
        },
        previewString: function(recipeCollection){
            return `${ recipeCollection.recipes[0].name }, ...`;
        }
    }
}
</script>

<style scoped>

</style>