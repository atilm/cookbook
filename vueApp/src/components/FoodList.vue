<template>
    <div id="foodList">
        <h1 class="mt-5">List of food:</h1>
        <button @click="updateList">Refresh</button>
        <ul class="list-unstyled">
            <li v-for="(food, index) in foodItems" :key="food.name">{{index + 1}} {{food.name}} ({{food.kcal}} kcal)</li>
        </ul>
    </div>
</template>

<script>
import FoodService from "../common/api.service";

export default {
    name: "FoodList",
    data() {
        return {
            foodItems: []
        };
    },
    mounted() {
        this.foodService = new FoodService();
        this.updateList();
    },
    methods: {
        updateList: function(){
            let vm = this;
            this.foodService.getAll().then(items => this.foodItems = items);
        }
    }
};
</script>

<style>

</style>