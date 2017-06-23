<template>
  <widget>
    <span slot="header">{{ textGroup.groupName }}</span>
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
  import fetch from 'universal-fetch';
  import xpath from 'xpath';
  import SyncLoader from 'vue-spinner/src/SyncLoader';
  import Widget from '@/components/Widget';
  import { sortBy } from '@/utils';

  export default {
    created() {
      this.fetchData();
    },
    computed: mapState({
      ctsURL: 'ctsURL',
      textGroup: 'ctsTextGroup',
    }),
    watch: {
      textGroup: 'fetchData',
    },
    data() {
      return {
        loading: false,
        works: null,
      };
    },
    methods: {
      fetchData() {
        this.loading = true;
        this.fetchTextGroup().then((works) => {
          this.works = works;
          this.loading = false;
        });
      },
      async fetchTextGroup() {
        const url = `${this.ctsURL}?request=GetCapabilities&urn=${this.textGroup.urn}`;
        const response = await fetch(url);
        const text = await response.text();
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(text, 'text/xml');
        const select = xpath.useNamespaces({ cts: 'http://chs.harvard.edu/xmlns/cts' });
        const works = [];
        select('//cts:TextInventory/cts:textgroup/cts:work', xmlDoc).forEach((work) => {
          const urn = select('@urn', work)[0].textContent;
          const title = select('cts:title', work)[0].textContent;
          works.push({ urn, title });
        });
        works.sort(sortBy('title', true, x => x.toUpperCase()));
        return works;
      },
      handleWorkClick(work) {
        this.$store.commit('setCtsWork', work);
      },
    },
    components: {
      Widget,
      SyncLoader,
    },
  };
</script>
