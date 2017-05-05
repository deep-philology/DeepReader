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
  },
  getters: {
    user: state => state.user,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
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
