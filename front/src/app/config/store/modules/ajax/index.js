import * as types from './types'
import * as getters from './getters'
import * as actions from './actions'

const state = {
  inProgress: 0
}

const mutations = {
  [types.BEGIN_AJAX_CALL] (state) {
    state.inProgress += 1
  },
  [types.AJAX_CALL_SUCCESS] (state) {
    state.inProgress -= 1
  },
  [types.AJAX_CALL_ERROR] (state) {
    state.inProgress -= 1
  }
}

export default {
  state,
  mutations,
  actions,
  getters
}
