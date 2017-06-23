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
  import fetch from 'universal-fetch';
  import xpath from 'xpath';
  import SyncLoader from 'vue-spinner/src/SyncLoader';
  import Widget from '@/components/Widget';
  import { sortBy } from '@/utils';

  export default {
    created() {
      this.fetchData().then((textGroups) => {
        this.textGroups = textGroups;
      });
    },
    computed: mapState(['ctsURL']),
    data() {
      return {
        loading: false,
        textGroups: null,
      };
    },
    methods: {
      async fetchData() {
        this.loading = true;
        const url = `${this.ctsURL}?request=GetCapabilities&urn=urn:cts:greekLit`;
        const response = await fetch(url);
        const text = await response.text();
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(text, 'text/xml');
        const select = xpath.useNamespaces({ cts: 'http://chs.harvard.edu/xmlns/cts' });
        // console.log(select('//cts:TextInventory/cts:textgroup', xmlDoc)[0]);
        const textGroups = [];
        select('//cts:TextInventory/cts:textgroup', xmlDoc).forEach((textGroup) => {
          const urn = select('@urn', textGroup)[0].textContent;
          const groupName = select('cts:groupname', textGroup)[0].textContent;
          textGroups.push({ urn, groupName });
        });
        textGroups.sort(sortBy('groupName', true, x => x.toUpperCase()));
        this.loading = false;
        return textGroups;
      },
      handleTextGroupClick(textGroup) {
        this.$store.commit('setCtsTextGroup', textGroup);
        this.$store.commit('setCtsWork', null);
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
