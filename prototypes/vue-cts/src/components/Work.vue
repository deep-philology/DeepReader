<template>
  <widget>
    <span slot="header">Work: {{ work.title }}</span>
    <div slot="body">
      <ul>
        <li class="click" v-for="edition in editions" @click="handleEditionClick(edition)">{{ edition.label }}</a></li>
      </ul>
    </div>
  </widget>
</template>

<script>
  import { mapGetters } from 'vuex';
  import fetch from 'universal-fetch';
  import xpath from 'xpath';
  import Widget from '@/components/Widget';

  export default {
    created() {
      this.fetchData();
    },
    computed: mapGetters({
      ctsURL: 'ctsURL',
      work: 'ctsWork',
    }),
    watch: {
      work: 'fetchData',
    },
    data() {
      return {
        editions: null,
      };
    },
    methods: {
      fetchData() {
        this.fetchEditions().then((editions) => {
          this.editions = editions;
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
    },
  };
</script>

<style lang="scss" scoped>
li {
  text-indent: -1em;
  margin-left: 1em;
}
</style>
