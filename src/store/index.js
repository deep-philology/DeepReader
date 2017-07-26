import Vue from 'vue';
import Vuex from 'vuex';
import { firebaseMutations, firebaseAction } from 'vuexfire';
import app from '@/firebase';
import cts from '@/store/cts';

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
    cts,
  },
  state: {
    user: null,
    book: null,
    interlinear: false,
    passage: null,
    textClasses: {},
    selectedWord: null,
  },
  getters: {
    textClasses(state) {
      return Object.entries(state.textClasses).reduce(
        (o, [k, v]) => {
          if (typeof v === 'boolean') {
            return Object.assign(o, { [k]: v });
          }
          return Object.assign(o, { [`${k}-${v}`]: true });
        },
        {},
      );
    },
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setReader(state, { book, passage }) {
      state.book = book;
      state.passage = passage;
    },
    setCTSReader(state, { passage }) {
      state.book = null;
      state.passage = passage;
    },
    toggleInterlinear(state) {
      state.interlinear = !state.interlinear;
    },
    setTextClass(state, classes) {
      state.textClasses = { ...state.textClasses, ...classes };
    },
    setSelectedWord(state, word) {
      state.selectedWord = word;
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
