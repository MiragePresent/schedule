<template>
  <div>
    <tasks-list></tasks-list>
  </div>
</template>

<script>
  import TasksList from './TasksList.vue'
  export default {
    name: 'ScheduleScreen',
    props: ['day'],
    components: {
      TasksList
    }
  }
</script>

<style lang="scss">
</style>
