<template>
    <div id="foodList">
        <h1 class="mt-5">List of food:</h1>
        <button @click="updateList">Refresh</button>
        <ul class="list-unstyled">
            <li v-for="(food) in foodItems" :key="food.id">{{food.id}} {{food.name}} ({{food.kcal}} kcal)
                <Button @click="deleteFood(food.id)">Delete</Button></li>
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
        },
        deleteFood: function(id){
            let vm = this;
            this.foodService.deleteFood(id).then(vm.updateList);
        }
    }
};
</script>

<style>

</style>