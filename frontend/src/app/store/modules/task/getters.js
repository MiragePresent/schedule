import moment from 'moment';

export default {
  tasks: state => state.tasks,
  editTask: state => state.editTask,
  selectedDate: (state) => {
    if (!state.selectedDate) {
      return moment().format('YYYY-MM-DD');
    }
    return state.selectedDate;
  },
}
