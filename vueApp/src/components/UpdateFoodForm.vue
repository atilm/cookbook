<template>
    <div v-if="food.id !== null">
        <form @submit.prevent="updateFood">
        <fieldset>
            <legend>Edit food</legend>
            <p>
            <label for="foodName">Name</label>
            <input v-model="currentFood.name" ref="fooodnameref" id="foodName">
            </p>
            <p>
            <label for="calories">kcal / 100 g</label>
            <input v-model="currentFood.kcal" id="calories">
            </p>
            <p>
            <button type="submit">Update</button>
            </p>
        </fieldset>
        </form>
        <p>Last updated: {{lastUpdated.name}} ({{lastUpdated.kcal}})</p>
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
            currentFood: this.food,
            lastUpdated: new Food()
        }
    },
    mounted() {
        this.foodService = new FoodService();
    },
    watch: {
        food: function(newVal, oldVal) {
            this.currentFood = newVal;
        }
    },
    methods: {
        updateFood: function(){
            this.foodService.updateFood(this.currentFood)
                .then(response => this.lastUpdated = response);
            this.currentFood = new Food();
            this.$refs.fooodnameref.focus();
        }
    }
}
</script>

<style>

</style>