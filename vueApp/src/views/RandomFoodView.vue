<template>
    <div class="container">
      <div class="row">
        <div class="col">
          <p>Five randomly choosen foods:</p>
          <ul>
              <li v-for="food in randomFoodItems" :key="food.id">{{food.name}}</li>
          </ul>
        </div>
      </div>
    </div>
</template>

<script>
import FoodService from "../common/foodService"

export default {
    name: 'random-food-view',
    data() {
        return {
            randomFoodItems: []
        }
    },
    mounted() {
        this.foodService = new FoodService();
        this.foodService.getRandomlyChosen(5)
            .then(foodItems => this.randomFoodItems = foodItems);
    }
}
</script>

<style>

</style>