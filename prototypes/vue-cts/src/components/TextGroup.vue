<template>
  <widget>
    <span slot="header">{{ textGroup.groupName }}</span>
    <div slot="body">
      <ul>
        <li class="click" v-for="work in works" @click="handleWorkClick(work)">{{ work.title }}</a></li>
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
      textGroup: 'ctsTextGroup',
    }),
    watch: {
      textGroup: 'fetchData',
    },
    data() {
      return {
        works: null,
      };
    },
    methods: {
      fetchData() {
        this.fetchTextGroup().then((works) => {
          this.works = works;
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
        works.sort((a, b) => {
          if (a.title < b.title) {
            return -1;
          }
          if (a.title > b.title) {
            return 1;
          }
          return 0;
        });
        return works;
      },
      handleWorkClick(work) {
        this.$store.commit('setCtsWork', work);
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
