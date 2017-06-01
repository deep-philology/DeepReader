<template>
  <widget>
    <span slot="header">Text Groups</span>
    <div slot="body">
      <ul>
        <li class="click" v-for="textGroup in textGroups" @click="handleTextGroupClick(textGroup)">{{ textGroup.groupName }}</a></li>
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
      this.fetchData().then((textGroups) => {
        this.textGroups = textGroups;
      });
    },
    computed: mapGetters(['ctsURL']),
    data() {
      return {
        textGroups: null,
      };
    },
    methods: {
      async fetchData() {
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
        textGroups.sort((a, b) => {
          if (a.groupName < b.groupName) {
            return -1;
          }
          if (a.groupName > b.groupName) {
            return 1;
          }
          return 0;
        });
        return textGroups;
      },
      handleTextGroupClick(textGroup) {
        this.$store.commit('setCtsTextGroup', textGroup);
        this.$store.commit('setCtsWork', null);
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
