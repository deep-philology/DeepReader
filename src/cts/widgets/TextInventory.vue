<template>
  <widget>
    <span slot="header">Text Groups</span>
    <div slot="body">
      <sync-loader v-if="loading" color="#000" size="5px" margin="3px" radius="100%"></sync-loader>
      <ul v-else>
        <li class="click hanging" v-for="textGroup in textGroups" @click="handleTextGroupClick(textGroup)">{{ textGroup.groupName }}</a></li>
      </ul>
    </div>
  </widget>
</template>

<script>
  import { mapState } from 'vuex';
  import SyncLoader from 'vue-spinner/src/SyncLoader';
  import Widget from '@/components/Widget';

  export default {
    computed: mapState({
      loading: state => state.cts.textGroupsLoading,
      textGroups: state => state.cts.textGroups,
    }),
    methods: {
      handleTextGroupClick(textGroup) {
        this.$store.commit('cts/setTextGroup', textGroup);
        this.$router.push({ query: { urn: textGroup.urn } });
      },
    },
    components: {
      Widget,
      SyncLoader,
    },
  };
</script>

<style lang="scss" scoped>
  .v-spinner {
    text-align: center;
  }
</style>
