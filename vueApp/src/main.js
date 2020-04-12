import Vue from 'vue';
import VueRouter from 'vue-router';
import VueSelect from 'vue-select';
import App from './App.vue';
import MonthChooser from './components/MonthChooser.vue';
import EditFoodView from './views/EditFoodView.vue';
import ListFoodView from './views/ListFoodView.vue';
import RandomFoodView from './views/RandomFoodView.vue';
import RecipeListView from './views/ListRecipesView.vue';
import RecipeDetailsView from './views/RecipeDetailsView.vue';
import EditRecipeView from './views/EditRecipeView.vue';
import RandomRecipesView from './views/RandomRecipesView.vue';
import 'vue-select/dist/vue-select.css';

Vue.use(VueRouter);

Vue.component('vue-select', VueSelect);
Vue.component('month-chooser', MonthChooser);

const routes = [
  { path: '/', redirect: '/recipeList' },
  { path: '/food/:id/edit', name: 'editFood', component: EditFoodView },
  { path: '/food/create', component: EditFoodView },
  { path: '/foodAdmin', component: ListFoodView },
  { path: '/randomFood', component: RandomFoodView },
  { path: '/recipeList', component: RecipeListView },
  { path: '/recipe/:id/details', name: 'recipeDetails', component: RecipeDetailsView },
  { path: '/recipe/:id/edit', name: 'editRecipe', component: EditRecipeView },
  { path: '/recipe/create', component: EditRecipeView },
  { path: '/randomRecipes', component: RandomRecipesView }
]

const router = new VueRouter({
  routes: routes
})

new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
});