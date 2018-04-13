import ScheduleScreen from './components/ScheduleScreen.vue'

export default {
  path: '/',
  name: 'Schedule',
  meta: {
    title: 'Schedule'
  },
  props: (route) => ({ day: route.query.day }),
  component: ScheduleScreen,
}
