<template>
  <div class="root">
    <header>
      <div class="reader-nav">
        <router-link to="cts">CTS API (Perseids)</router-link>
        &bull;
        <router-link to="cite-services">cite-services</router-link>
        &bull;
        <router-link to="morphgnt">MorphGNT API</router-link>
      </div>
      <h1>DeepReader (CTS)</h1>
    </header>
    <div class="grid-wrapper">
      <div class="left">
        <text-inventory></text-inventory>
        <text-group v-if="ctsTextGroup"></text-group>
        <work v-if="ctsWork"></work>
      </div>

      <div class="main">
        <passage :linker="passageLink"></passage>
      </div>

      <div class="right">
        <text-formatting></text-formatting>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import xpath from 'xpath';
import fetch from 'universal-fetch';
import Passage from '@/components/Passage';
import TextFormatting from '@/components/TextFormatting';

import TextInventory from '@/cts/components/TextInventory';
import TextGroup from '@/cts/components/TextGroup';
import Work from '@/cts/components/Work';
import teiXSL from '@/cts/tei.xsl';


export default {
  name: 'reader',
  created() {
    this.$store.commit('setCTSReader', { passage: null });
    this.fetchData();
  },
  data() {
    return {
      query: null,
    };
  },
  computed: {
    ...mapState(['user', 'ctsTextGroup', 'ctsWork']),
  },
  watch: {
    $route: 'fetchData',
  },
  methods: {
    fetchData() {
      this.asyncData({ query: this.$route.query }).then(({ query, passage }) => {
        this.query = query;
        this.$store.commit('setCTSReader', { passage });
      });
    },
    async asyncData({ query }) {
      const urn = query.urn;
      const url = `http://cts.perseids.org/api/cts/?request=GetPassagePlus&urn=${urn}`;
      const response = await fetch(url);
      const text = await response.text();
      const parser = new DOMParser();
      const xmlDoc = parser.parseFromString(text, 'text/xml');
      const xsltProcessor = new XSLTProcessor();
      const xslDoc = parser.parseFromString(teiXSL, 'text/xml');
      xsltProcessor.importStylesheet(xslDoc);
      const select = xpath.useNamespaces({ cts: 'http://chs.harvard.edu/xmlns/cts' });
      const fragment = xsltProcessor.transformToFragment(xmlDoc, document);
      const passage = {
        fragment,
        next: select('//cts:prevnext/cts:next/cts:urn', xmlDoc)[0].textContent,
        prev: select('//cts:prevnext/cts:prev/cts:urn', xmlDoc)[0].textContent,
      };
      return { query, passage };
    },
    passageLink(urn) {
      const { query } = this;
      if (urn) {
        return {
          query: Object.assign({}, query, { urn }),
        };
      }
      return null;
    },
  },
  components: {
    Passage,
    TextFormatting,
    TextInventory,
    TextGroup,
    Work,
  },
};
</script>

<style lang="scss">

  /* TEI */

  .TEI {
    .milestone {
      color: #999;
      font-family: $widget-font-family;
      font-size: 60%;
    }
    .said {
      .label {
        font-weight: bold;
      }
    }
    .l .n {
      color: #999;
      font-family: $widget-font-family;
      font-size: 60%;
    }
  }
</style>
