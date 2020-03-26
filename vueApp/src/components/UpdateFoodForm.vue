<template>
    <div v-if="food.id !== null">
        <form @submit.prevent="updateFood">
        <fieldset>
            <legend>Edit food</legend>
            <p>
            <label for="foodName">Name</label>
            <input v-model="food.name" ref="fooodnameref" id="foodName">
            </p>
            <p>
            <label for="calories">kcal / 100 g</label>
            <input v-model="food.kcal" id="calories">
            </p>
            <p>
            <button type="submit">Update</button>
            </p>
        </fieldset>
        </form>
        <p>Last updated: {{lastUpdate.name}} ({{lastUpdate.kcal}})</p>
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
            lastUpdate: new Food()
        }
    },
    methods: {
        updateFood: function(){
            this.lastUpdate = this.food;
            this.food = new Food();
            this.$refs.fooodnameref.focus();
        }
    }
}
</script>

<style>

</style>