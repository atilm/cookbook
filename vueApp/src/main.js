import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App.vue';
import FoodList from './components/FoodList.vue';
import AddFoodForm from './components/AddFoodForm.vue';
import UpdateFoodForm from './components/UpdateFoodForm.vue';
import MonthChooser from './components/MonthChooser.vue';
import FoodAdminView from './views/FoodAdminView.vue';
import RandomFoodView from './views/RandomFoodView.vue';
import RecipeListView from './views/ListRecipesView.vue';

Vue.use(VueRouter);

Vue.component('food-list', FoodList);
Vue.component('add-food-form', AddFoodForm);
Vue.component('update-food-form', UpdateFoodForm);
Vue.component('month-chooser', MonthChooser);

const routes = [
  { path: '/', redirect: '/randomFood' },
  { path: '/foodAdmin', component: FoodAdminView },
  { path: '/randomFood', component: RandomFoodView },
  { path: '/recipeList', component: RecipeListView}
]

const router = new VueRouter({
  routes: routes
})

new Vue({
  el: '#app',
  router: router,
  render: h => h(App)
});