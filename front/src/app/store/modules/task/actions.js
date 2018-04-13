import axios from 'axios'
import { API_URL } from '../../../config/base'
import {
  SET_TASKS,
  SET_EDIT_TASK,
  CREATE_TASK,
  UPDATE_TASK,
  DELETE_TASK,
} from './types'

export default {
  fetchTasks({ commit }) {
    let url = `http://${API_URL}/api/tasks/`;
    return axios.get(url)
      .then((response) => {
        commit(SET_TASKS, { tasks: response.data })
        return response
      })
      .catch((error) => {
        commit(SET_TASKS, { tasks: [] })
        return error
      })
  },
  createTask({ commit }, { uuid, title }) {
    let url = `http://${API_URL}/api/tasks/`;
    return axios.post(url, { title })
      .then(({ data }) => {
        commit(UPDATE_TASK, { task_id: uuid, data });
      });
  },
  updateTask({ commit }, { task_id, data }) {
    let url = `http://${API_URL}/api/tasks/${task_id}/`;
    return axios.patch(url, data)
      .then(({ data }) => {
        commit(UPDATE_TASK, { task_id, data })
      })
      .catch((error) => {
        return error;
      })
  },
  deleteTask({ commit }, task_id) {
    if (parseInt(task_id) == task_id) {
      let url = `http://${API_URL}/api/tasks/${task_id}/`;
      axios.delete(url)
        .then((response) => {
          commit(DELETE_TASK, task_id);
        })
        .catch((error) => {

        })
    } else {
      commit(DELETE_TASK, task_id);
    }
  },
  emptyTask({ commit }, data) {
    commit(CREATE_TASK, data);
  },
  setEdit({ commit }, task_id) {
    commit(SET_EDIT_TASK, task_id);
  }
};
