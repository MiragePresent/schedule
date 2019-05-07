<template>
  <div>
    <task-list></task-list>
  </div>
</template>

<script>
  import TaskList from './TaskList.vue'
  export default {
    name: 'TodoScreen',
    props: ['day'],
    components: {
      TaskList
    }
  }
</script>

<style lang="scss">
</style>
