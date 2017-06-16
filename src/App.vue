<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import store from '@/store';

export default {
  name: 'app',
  store,
  created() {
    this.$store.dispatch('authenticate');
  },
};
</script>

<style lang="scss">
  body {
    margin: 0;
    -webkit-font-smoothing: antialiased;
  }

  .click {
    color: inherit;
    text-decoration: none;
    cursor: pointer;
    &:hover {
      color: #666;
    }
  }
</style>
