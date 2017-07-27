<template>
  <widget>
    <span slot="header">Text Group: {{ textGroup.groupName }}</span>
    <div slot="body">
      <sync-loader v-if="loading" color="#000" size="5px" margin="3px" radius="100%"></sync-loader>
      <ul v-else>
        <li class="click hanging" v-for="work in works" @click="handleWorkClick(work)">{{ work.title }}</a></li>
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
      loading: state => state.cts.textGroupLoading,
      textGroup: state => state.cts.textGroup,
      works: state => state.cts.works,
    }),
    methods: {
      handleWorkClick(work) {
        this.$store.commit('cts/setWork', work);
        this.$router.push({ query: { urn: work.urn } });
      },
    },
    components: {
      Widget,
      SyncLoader,
    },
  };
</script>
