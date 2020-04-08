<template>
    <div class="container">
        <div class="row">
            <div class="col">
                <form @submit.prevent="saveFood">
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
                        <div class="form-group">
                            <label for="seasonMonthChooser">Season months</label>
                            <month-chooser id="seasonMonthChooser" v-model="currentFood.seasonMonths"/>
                        </div>
                        <div>
                            <button type="submit" class="btn btn-primary">Save</button>
                        </div>
                    </fieldset>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import FoodService from "../common/foodService";
import Food from "../common/food";

export default {
    name: "edit-food-view",
    data() {
        return {
            currentFood: new Food()
        }
    },
    mounted() {
        this.foodService = new FoodService();
        this.loadFood(this.$route.params.id);
    },
    methods: {
        saveFood: function() {
            if (this.currentFood.id === null)
                this.foodService.create(this.currentFood);
            else
                this.foodService.update(this.currentFood);

            this.$refs.fooodnameref.focus();
        },
        loadFood: function(id) {
            let vm = this;
            
            if (id === null) {
                this.currentFood = new Food();
            }
            else
                this.foodService.get(id).then(food => this.currentFood = food);
        }
    }
}
</script>

<style scoped>

</style>