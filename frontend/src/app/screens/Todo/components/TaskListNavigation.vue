<template>
  <v-layout>
    <v-btn
      icon
      @click="prevDay()"
    >
      <v-icon>keyboard_arrow_left</v-icon>
    </v-btn>
    <div class="nav-title">
      <h3>{{ title }}</h3>
    </div>
    <v-btn
      icon
      @click="nextDay()"
    >
      <v-icon>keyboard_arrow_right</v-icon>
    </v-btn>
  </v-layout>
</template>
<script>
import moment from 'moment';
import { mapGetters, mapActions } from 'vuex';
export default {
  computed: {
    ...mapGetters('task', ['selectedDate']),
    title() {
      if (this.selectedDate === moment().format('YYYY-MM-DD')) {
        return 'Today';
      }
      return moment(this.selectedDate, 'YYYY-MM-DD').format('MMMM Do');
    }
  },
  methods: {
    ...mapActions('task', [ 'setSelectedDate' ]),
    prevDay() {
      this.setSelectedDate(moment(this.selectedDate, 'YYYY-MM-DD').subtract(1, 'days').format("YYYY-MM-DD"));
    },
    nextDay() {
      this.setSelectedDate(moment(this.selectedDate, 'YYYY-MM-DD').add(1, 'days').format("YYYY-MM-DD"));
    },
  }
}
</script>

<style lang="css">
  .nav-title{
    padding-top: 12px
  }
</style>
