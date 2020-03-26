import Vue from 'vue';
import App from './App.vue';
import FoodList from './components/FoodList.vue';
import AddFoodForm from './components/AddFoodForm.vue';
import UpdateFoodForm from './components/UpdateFoodForm.vue';

Vue.component('food-list', FoodList);
Vue.component('add-food-form', AddFoodForm);
Vue.component('update-food-form', UpdateFoodForm);

new Vue({
  el: '#app',
  render: h => h(App),
});