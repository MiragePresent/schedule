import { SET_CLIENT_HEIGHT } from './types';

export default {
  [SET_CLIENT_HEIGHT](state, { height }) {
    state.height = height;
    return state.height;
  }
}
