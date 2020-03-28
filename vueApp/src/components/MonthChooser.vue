<template>
    <form class="form-inline">
        <div v-for="month in allMonths" :key="month" class="form-group">
            <label>{{month}}</label><br/>
            <input type="checkbox" :id="month" :value="month" v-model="checkedMonths" v-on:change="$emit('input', checkedMonths)">
        </div>
        <button class="btn-secondary btn-sm" @click.prevent="uncheckAll">Uncheck all</button>
    </form>
</template>

<script>
export default {
    name: "month-chooser",
    props: ["value"],
    data() {
        return {
            "checkedMonths": [...this.value],
            "allMonths": ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        }
    },
    watch: {
        value: function(newVal, oldVal) {
            this.checkedMonths = [...newVal];
        }
    },
    methods: {
        uncheckAll: function() {
            this.checkedMonths = [];
            this.$emit('input', this.checkedMonths)
        }
    }
}
</script>

<style scoped>
</style>