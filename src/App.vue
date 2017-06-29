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
    this.$log.log('App.vue created');
    this.$store.dispatch('authenticate');
  },
};
</script>

<style lang="scss">

  @import 'styles/common.scss';
  @import 'styles/skeleton.scss';

</style>
