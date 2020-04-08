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
import 'vue-select/dist/vue-select.css';

Vue.use(VueRouter);

Vue.component('vue-select', VueSelect);
Vue.component('month-chooser', MonthChooser);

const routes = [
  { path: '/', redirect: '/randomFood' },
  { path: '/food/:id/edit', name: 'editFood', component: EditFoodView },
  { path: '/foodAdmin', component: FoodAdminView },
  { path: '/randomFood', component: RandomFoodView },
  { path: '/recipeList', component: RecipeListView},
  { path: '/recipe/:id/details', name: 'recipeDetails', component: RecipeDetailsView},
  { path: '/recipe/:id/edit', name: 'editRecipe', component: EditRecipeView}
]

const router = new VueRouter({
  routes: routes
})

new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
});