<template>
    <div class="container">
      <div class="row">
        <div class="col">
          <form @submit.prevent="createRecipe">
            <legend>Create Recipe</legend>
            <div class="form-group">
                <label for="recipeName">Name</label>
                <input type="text" class="form-control" id="recipeName" v-model="currentRecipe.name">
            </div>
            <button type="submit" class="btn btn-primary">Create</button>
        </form>
        <p>Last created: {{lastCreated.name}})</p>
        </div>
      </div>
    </div>
</template>

<script>
export default {
    name: 'add-recipe-view',
    data() {
        return {
            currentRecipe = { 'name' : ""},
            lastCreated = 
        }
    }
}
</script>

<style>

</style>