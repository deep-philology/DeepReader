<template>
  <div class="root">
    <header>
      <div class="reader-nav">
        <router-link to="cts">CTS API (Perseids)</router-link>
        &bull;
        <router-link to="cite-services">cite-services</router-link>
        &bull;
        <router-link to="morphgnt">MorphGNT API</router-link>
      </div>
      <h1>DeepReader (Github)</h1>
    </header>
    <div class="grid-wrapper">
      <div class="left">
        <action-select :actions="actions"></action-select>
        <issue-select :issues="issues"></issue-select>
      </div>

      <div class="main">
      </div>

      <div class="right">
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import ActionSelect from '@/Github/components/ActionSelect';
import IssueSelect from '@/Github/components/IssueSelect';

import Github from '@/Github';

export default {
  name: 'reader',
  created() {
    this.$store.commit('setReader', { issue: null });
    this.fetchData();
  },
  data() {
    return {
      issues: [],
      actions: ['Issues'],
    };
  },
  computed: {
    ...mapState(['user']),
  },
  watch: {
    $route: 'fetchData',
  },
  methods: {
    fetchData() {
      this.asyncData().then(({ issues }) => {
        this.issues = issues;
      });
      // this.$log.log('fetchData() issues = ', issues);
      // return issues;
    },
    async asyncData() {
      const issues = await Github.issues();
      return { issues };
    },
  },
  components: {
    ActionSelect,
    IssueSelect,
  },
};
</script>
