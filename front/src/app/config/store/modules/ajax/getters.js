export const isLoading = (state, getters, rootState) => {
  return state.inProgress > 0
}
