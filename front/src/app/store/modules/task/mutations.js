import {
  SET_TASKS,
  SET_EDIT_TASK,
  UPDATE_TASK,
  CREATE_TASK,
  DELETE_TASK,
} from './types';

export default {
  [SET_TASKS](state, {tasks}) {
    Object.assign(state, {tasks});
    return state.library;
  },
  [SET_EDIT_TASK](state, task_id) {
    state.editTask = task_id;
    return state.editTask;
  },
  [CREATE_TASK](state, taskData) {
    state.tasks.push(taskData);
    return taskData;
  },
  [UPDATE_TASK](state, { task_id, data }) {
    let index = state.tasks.findIndex(task => task.id == task_id);
    state.tasks[index] = Object.assign(state.tasks[index], data);
    return state.tasks[index];
  },
  [DELETE_TASK](state, task_id) {
    state.tasks = state.tasks.filter(task => task.id != task_id);
  }
}
