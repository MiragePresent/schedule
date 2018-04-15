import moment from 'moment';

export default {
  selectedDate: (state) => {
    if (!state.selectedDate) {
      return moment().format('YYYY-MM-DD');
    }
    return state.selectedDate;
  },
  tasks: (state, getters) => state.tasks.filter(task => task.date == getters.selectedDate),
  editTask: state => state.editTask,
}
