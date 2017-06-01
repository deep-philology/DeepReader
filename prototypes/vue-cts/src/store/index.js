import Vue from 'vue';
import Vuex from 'vuex';
import { firebaseMutations, firebaseAction } from 'vuexfire';
import app from '@/firebase';

Vue.use(Vuex);

/* eslint-disable no-new */
export default new Vuex.Store({
  modules: {
    bookmarkList: {
      state: {
        bookmarks: [],
      },
      getters: {
        bookmarks: state => state.bookmarks,
      },
      actions: {
        setBookmarksRef: firebaseAction(({ bindFirebaseRef }, ref) => {
          bindFirebaseRef('bookmarks', ref);
        }),
      },
    },
  },
  state: {
    user: null,
    ctsURL: 'http://cts.perseids.org/api/cts/',
    ctsTextGroup: '',
    ctsWork: '',
    passage: null,
    textSize: 'normal',
  },
  getters: {
    user: state => state.user,
    ctsURL: state => state.ctsURL,
    ctsTextGroup: state => state.ctsTextGroup,
    ctsWork: state => state.ctsWork,
    passage: state => state.passage,
    textSize: state => state.textSize,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setCtsTextGroup(state, textGroup) {
      state.ctsTextGroup = textGroup;
    },
    setCtsWork(state, work) {
      state.ctsWork = work;
    },
    setReader(state, { passage }) {
      state.passage = passage;
    },
    setTextSize(state, size) {
      state.textSize = size;
    },
    ...firebaseMutations,
  },
  actions: {
    async authenticate({ commit }) {
      await app.auth().onAuthStateChanged((user) => {
        if (user) {
          commit('setUser', user);
        } else {
          app.auth().signInAnonymously();
        }
      });
    },
  },
});
