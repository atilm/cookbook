<template>
  <div class="container">
      <div class="row">
        <div class="col">   
          <h2>List of food <button class="btn btn-dark btn-sm" @click="updateList">Refresh</button></h2>
          <form @submit.prevent="searchFood" class="form-inline mb-2">
              <div class="form-group">
                  <input type="text" class="form-control" v-model="searchTerm"/>
              </div>
              <div class="form-group">
                  <Button type="submit" class="btn btn-primary ml-2">Search</Button>
              </div>
          </form>
        </div>
      </div>
      <div class="row">
        <div class="col">  
            <table class="table">
                <tbody>
                    <tr  v-for="(food) in foodItems" :key="food.id">
                        <td><router-link :to="{ name: 'editFood', params: { id: food.id }}">{{food.name}}</router-link></td>
                        <td>({{food.kcal}} kcal)</td>
                        <td><div v-html="monthString(food)"/></td>
                        <td><Button @click="deleteFood(food.id)" class="btn btn-secondary btn-sm">Delete</Button></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
  </div>
</template>

<script>
import FoodService from "../common/foodService";
import Food from "../common/food";

export default {
    name: "list-food-view",
    data() {
        return {
            foodItems: [],
            searchTerm: ""
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
        searchFood: function(){
            let vm = this;
            this.foodService.getBySearchTerm(this.searchTerm)
                .then(items => this.foodItems = items);
        },
        deleteFood: function(id){
            let vm = this;
            this.foodService.delete(id).then(vm.updateList);
        },
        monthString: function(food){
            let allMonths = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
            let result = "";

            for (let i = 0; i < allMonths.length; i++) {
                let monthString = allMonths[i];
                if (food.seasonMonths.includes(monthString)){
                    result += "<b>" + monthString[0] + "</b>";
                }
                else {
                    result += monthString[0];
                }
            }

            return result;
        }
    }
};
</script>

<style>

</style>