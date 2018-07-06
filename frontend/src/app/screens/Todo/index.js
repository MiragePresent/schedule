import ScheduleScreen from './components/TodoScreen.vue'

export default {
  path: '/',
  name: 'Todo',
  meta: {
    title: 'TODO'
  },
  props: (route) => ({ day: route.query.day }),
  component: ScheduleScreen,
}
