import Vue from 'vue';
import App from './App.vue';
import FoodList from './components/FoodList.vue';

Vue.component('food-list', FoodList);

new Vue({
  el: '#app',
  render: h => h(App),
});