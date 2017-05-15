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
    book: null,
    passage: null,
    textSize: 'normal',
    interlinear: false,
    colour: null,
  },
  getters: {
    user: state => state.user,
    book: state => state.book,
    passage: state => state.passage,
    textSize: state => state.textSize,
    interlinear: state => state.interlinear,
    colour: state => state.colour,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setReader(state, { book, passage }) {
      state.book = book;
      state.passage = passage;
    },
    setTextSize(state, size) {
      state.textSize = size;
    },
    toggleInterlinear(state) {
      state.interlinear = !state.interlinear;
    },
    setColour(state, scheme) {
      state.colour = scheme;
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
