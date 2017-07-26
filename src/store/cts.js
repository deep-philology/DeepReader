/* eslint-disable no-shadow */
import cts from '@/cts';

const state = {
  textGroups: null,
  works: null,
  editions: null,

  textGroup: null,
  work: null,

  textGroupsLoading: false,
  textGroupLoading: false,
  workLoading: false,
};

const actions = {
  loadTextGroups({ commit, state }, urn) {
    state.textGroupsLoading = true;
    cts.textGroups(urn).then((textGroups) => {
      commit('setTextGroups', textGroups);
      state.textGroupsLoading = false;
    });
  },
  loadTextGroup({ commit, state }, urn) {
    state.textGroupLoading = true;
    cts.textGroup(urn).then((works) => {
      commit('setWorks', works);
      state.textGroupLoading = false;
    });
  },
  loadWork({ commit, state }, urn) {
    state.workLoading = true;
    cts.work(urn).then((editions) => {
      commit('setEditions', editions);
      state.workLoading = false;
    });
  },
};

const mutations = {
  setTextGroups(state, textGroups) {
    state.textGroups = textGroups;
  },
  setWorks(state, works) {
    state.works = works;
  },
  setEditions(state, editions) {
    state.editions = editions;
  },
  setTextGroup(state, textGroup) {
    state.textGroup = textGroup;
  },
  setWork(state, work) {
    state.work = work;
  },
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
};
