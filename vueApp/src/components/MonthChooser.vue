<template>
    <form class="form-inline">
        <div v-for="month in allMonths" :key="month" class="form-group">
            <label>{{month}}</label><br/>
            <input type="checkbox" :id="month" :value="month" v-model="value" v-on:change="$emit('input', value)">
        </div>
    </form>
</template>

<script>
export default {
    name: "month-chooser",
    props: ["value"],
    data() {
        return {
            "checkedMonths": [],
            "allMonths": ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        }
    }
}
</script>

<style scoped>
</style>