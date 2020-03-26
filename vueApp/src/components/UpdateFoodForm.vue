<template>
    <div v-if="currentFood.id !== null">
        <form @submit.prevent="updateFood">
        <fieldset>
            <legend>Edit food</legend>
            <div class="form-group">
                <label for="foodName">Name</label>
                <input type="text" class="form-control" id="foodName" v-model="currentFood.name" ref="fooodnameref">
            </div>
            <div class="form-group">
                <label for="calories">kcal / 100 g</label>
                <input type="number" class="form-control" id="calories" v-model="currentFood.kcal">
            </div>
            <div>
            <button type="submit" class="btn btn-primary">Update</button>
            <button class="btn btn-secondary" @click="cancel">Cancel</button>
            </div>
        </fieldset>
        </form>
    </div>
</template>

<script>
import FoodService from "../common/api.service";
import Food from "../common/food";

export default {
    name: "update-food-form",
    props: ["food"],
    data() {
        return {
            currentFood: new Food()
        }
    },
    mounted() {
        this.foodService = new FoodService();
    },
    watch: {
        food: function(newVal, oldVal) {
            this.currentFood = Object.assign({}, newVal);
        }
    },
    methods: {
        updateFood: function(){
            this.foodService.updateFood(this.currentFood)
                .then(response => this.lastUpdated = response);
            this.currentFood = new Food();
        },
        cancel: function(){
            this.currentFood = new Food();
        }
    }
}
</script>

<style>

</style>