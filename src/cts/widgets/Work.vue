<template>
  <widget>
    <span slot="header">Work: {{ work.title }}</span>
    <div slot="body">
      <sync-loader v-if="loading" color="#000" size="5px" margin="3px" radius="100%"></sync-loader>
      <ul v-else>
        <li class="click hanging" v-for="edition in editions" @click="handleEditionClick(edition)">{{ edition.label }}</a></li>
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
      loading: state => state.cts.workLoading,
      work: state => state.cts.work,
      editions: state => state.cts.editions,
    }),
    methods: {
      handleEditionClick(edition) {
        this.fetchEdition(edition).then((urn) => {
          this.$router.push({ query: { urn } });
        });
      },
    },
    components: {
      Widget,
      SyncLoader,
    },
  };
</script>
