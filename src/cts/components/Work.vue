<template>
  <widget>
    <span slot="header">Work: {{ work.title }}</span>
    <div slot="body">
      <sync-loader v-if="loading" color="#000" size="5px" margin="3px" radius="100%"></sync-loader>
      <ul v-else>
        <li class="click" v-for="edition in editions" @click="handleEditionClick(edition)">{{ edition.label }}</a></li>
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

  export default {
    created() {
      this.fetchData();
    },
    computed: mapState({
      ctsURL: 'ctsURL',
      work: 'ctsWork',
    }),
    watch: {
      work: 'fetchData',
    },
    data() {
      return {
        loading: false,
        editions: null,
      };
    },
    methods: {
      fetchData() {
        this.loading = true;
        this.fetchEditions().then((editions) => {
          this.editions = editions;
          this.loading = false;
        });
      },
      async fetchEditions() {
        const url = `${this.ctsURL}?request=GetCapabilities&urn=${this.work.urn}`;
        const response = await fetch(url);
        const text = await response.text();
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(text, 'text/xml');
        const select = xpath.useNamespaces({ cts: 'http://chs.harvard.edu/xmlns/cts' });
        const editions = [];
        select('//cts:TextInventory/cts:textgroup/cts:work/cts:edition', xmlDoc).forEach((work) => {
          const urn = select('@urn', work)[0].textContent;
          const label = select('cts:label', work)[0].textContent;
          editions.push({ urn, label });
        });
        return editions;
      },
      async fetchEdition(edition) {
        const url = `${this.ctsURL}?request=GetValidReff&urn=${edition.urn}`;
        const response = await fetch(url);
        const text = await response.text();
        const parser = new DOMParser();
        const xmlDoc = parser.parseFromString(text, 'text/xml');
        const select = xpath.useNamespaces({ cts: 'http://chs.harvard.edu/xmlns/cts' });
        return select('//cts:reff/cts:urn', xmlDoc)[0].textContent;
      },
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

<style lang="scss" scoped>
li {
  text-indent: -1em;
  margin-left: 1em;
}
</style>
