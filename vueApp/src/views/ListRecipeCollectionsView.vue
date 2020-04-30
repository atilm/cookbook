<template>
    <table class="table">
        <tbody>
            <tr :v-for="collection in recipeCollections" :key="collection.id">
                <td>{{collection.date}}</td>
                <td>{{listNames(collection)}}</td>
            </tr>
        </tbody>
    </table>
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
        listNames: function(recipeCollection){
            return recipeCollection.recipeIds.join(", ")
        }
    }
}
</script>

<style scoped>

</style>