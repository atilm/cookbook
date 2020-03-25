<template>
    <div>
        <form @submit.prevent="createFood">
        <fieldset>
            <legend>New food</legend>
            <p>
            <label for="foodName">Name</label>
            <input v-model="currentFood.name" ref="fooodnameref" id="foodName">
            </p>
            <p>
            <label for="calories">kcal / 100 g</label>
            <input v-model="currentFood.kcal" id="calories">
            </p>
            <p>
            <button type="submit">Create</button>
            </p>
        </fieldset>
        </form>
        <p>Last created: {{lastCreated.name}} ({{lastCreated.kcal}})</p>
    </div>
</template>

<script>
import FoodService from "../common/api.service";

export default {
    name: "add-food-form",
    data() {
        return {
            currentFood: {"id": 0, "name": "", "kcal": ""},
            lastCreated: {"id": 0, "name": "", "kcal": ""}
        };
    },
    mounted() {
        this.foodService = new FoodService();
    },
    methods: {
        createFood: function(){
            this.foodService.createFood(this.currentFood)
                .then(response => this.lastCreated = response);
            this.currentFood = {"id": 0, "name": "", "kcal": ""};
            this.$refs.fooodnameref.focus();
        }
    }
}
</script>

<style>

</style>