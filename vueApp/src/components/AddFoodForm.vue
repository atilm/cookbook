<template>
    <div>
        <form @submit.prevent="createFood">
            <legend>Create Food</legend>
            <div class="form-group">
                <label for="foodName">Name</label>
                <input type="text" class="form-control" id="foodName" v-model="currentFood.name" ref="fooodnameref">
            </div>
            <div class="form-group">
                <label for="calories">kcal / 100 g</label>
                <input type="number" class="form-control" id="calories" v-model="currentFood.kcal">
            </div>
            <button type="submit" class="btn btn-primary">Create</button>
        </form>
        <p>Last created: {{lastCreated.name}} ({{lastCreated.kcal}})</p>
    </div>
</template>

<script>
import FoodService from "../common/api.service";
import Food from "../common/food";

export default {
    name: "add-food-form",
    data() {
        return {
            currentFood: new Food(),
            lastCreated: new Food()
        };
    },
    mounted() {
        this.foodService = new FoodService();
    },
    methods: {
        createFood: function(){
            this.foodService.createFood(this.currentFood)
                .then(response => this.lastCreated = response);
            this.currentFood = new Food();
            this.$refs.fooodnameref.focus();
        }
    }
}
</script>

<style>

</style>