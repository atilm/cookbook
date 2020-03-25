import Vue from 'vue';
import App from './App.vue';
import FoodList from './components/FoodList.vue';
import AddFoodForm from './components/AddFoodForm.vue';

Vue.component('food-list', FoodList);
Vue.component('add-food-form', AddFoodForm);

new Vue({
  el: '#app',
  render: h => h(App),
});