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
    interlinear: false,
    ctsURL: 'http://cts.perseids.org/api/cts/',
    ctsTextGroup: '',
    ctsWork: '',
    passage: null,
    textClasses: {},
  },
  getters: {
    user: state => state.user,
    book: state => state.book,
    ctsURL: state => state.ctsURL,
    ctsTextGroup: state => state.ctsTextGroup,
    ctsWork: state => state.ctsWork,
    passage: state => state.passage,
    interlinear: state => state.interlinear,
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
    setCtsTextGroup(state, textGroup) {
      state.ctsTextGroup = textGroup;
    },
    setCtsWork(state, work) {
      state.ctsWork = work;
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
