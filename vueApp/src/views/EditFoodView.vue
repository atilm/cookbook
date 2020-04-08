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
                <div v-if="lastSaved.id" class="alert alert-primary" role="alert">
                    Saved food {{lastSaved.name}}.
                    <button type="button" class="close" @click="dismissNotification" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
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
            lastSaved: new Food(),
            currentFood: new Food(),
            dismissCountDown: 0
        }
    },
    mounted() {
        this.foodService = new FoodService();
        this.loadFood(this.$route.params.id);
    },
    methods: {
        saveFood: function() {
            if (this.currentFood.id === null) {
                this.foodService.create(this.currentFood)
                .then(food => this.lastSaved = food);
            }
            else {
                this.foodService.update(this.currentFood)
                .then(food => this.lastSaved = food);
            }

            this.$refs.fooodnameref.focus();
        },
        loadFood: function(id) {
            let vm = this;
            
            if (id === null) {
                this.currentFood = new Food();
            }
            else
                this.foodService.get(id).then(food => this.currentFood = food);
        },
        dismissNotification: function() {
            this.lastSaved = new Food();
        }
    }
}
</script>

<style scoped>

</style>