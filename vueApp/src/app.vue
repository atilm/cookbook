<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
      <div class="container">
        <a class="navbar-brand" href="#">Cookbook</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <router-link class="nav-link" to="/recipeList">Search Recipes</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/recipe/create">Create Recipe</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/food/create">Create Food</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/foodAdmin">Search Food</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/randomFood">Five random foods</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/randomRecipes">Random recipes</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/recipeCollections">Recipe collections</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <router-view></router-view>
  </div>
</template>

<script>
export default {
};
</script>

<style>
</style>