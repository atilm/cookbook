<template>
    <div id="foodList">
        <update-food-form :food="foodToUpdate" />
        <h1 class="mt-5">List of food:</h1>
        <button @click="updateList">Refresh</button>
        <ul class="list-unstyled">
            <li v-for="(food) in foodItems" :key="food.id">{{food.id}} {{food.name}} ({{food.kcal}} kcal)
                <Button @click="deleteFood(food.id)">Delete</Button>
                <Button @click="editFood(food)">Edit</Button></li>
        </ul>
    </div>
</template>

<script>
import FoodService from "../common/api.service";
import Food from "../common/food";

export default {
    name: "FoodList",
    data() {
        return {
            foodItems: [],
            foodToUpdate: new Food()
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
        },
        deleteFood: function(id){
            let vm = this;
            this.foodService.deleteFood(id).then(vm.updateList);
        },
        editFood: function(food){
            this.foodToUpdate = food;
        }
    }
};
</script>

<style>

</style>