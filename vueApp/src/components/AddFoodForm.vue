<template>
    <div>
        <form @submit.prevent="createFood">
        <fieldset>
            <legend>New food</legend>
            <p>
            <input v-model="currentFood.name" ref="fooodnameref" id="foodName">
            <label for="foodName">Name</label>
            </p>
            <p>
            <input v-model="currentFood.kcal" id="calories">
            <label for="calories">kcal / 100 g</label>
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
import { FoodService } from "../common/api.service";

export default {
    name: "add-food-form",
    data() {
        return {
            currentFood: {"name": "", "kcal": ""},
            lastCreated: {"name": "", "kcal": ""}
        };
    },
    methods: {
        createFood: function(){
            this.lastCreated = this.currentFood;
            this.currentFood = {"name": "", "kcal": ""};
            this.$refs.fooodnameref.focus();
        }
    }
}
</script>

<style>

</style>