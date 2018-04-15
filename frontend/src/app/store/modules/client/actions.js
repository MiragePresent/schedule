import { SET_CLIENT_HEIGHT } from './types'

export default {
  setHeight({ commit }, height) {
    commit(SET_CLIENT_HEIGHT, { height: height });
  },
}
