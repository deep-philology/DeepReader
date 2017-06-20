<template>
  <div class="root">
    <header>
      <div class="reader-nav">
        <a href="/#/cts/">CTS API (Perseids)</a>
        &bull;
        <a href="/#/cite-services/">cite-services</a>
        &bull;
        <a href="/#/morphgnt/">MorphGNT API</a>
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
  /* hover opacity */

  .widget, .root > header, .page-nav-1 {
    opacity: 0;
    transition: opacity 0.5s ease-in-out;
  }

  body:hover {
    .widget, .root > header, .page-nav-1 {
      opacity: 1;
    }
  }

  /* grid */

  .grid-wrapper {
    display: grid;
    grid-template-columns: 2fr 6fr 4fr;
    grid-column-gap: 10px;
    margin: 10px;
    > * {
      min-width: 200px;
    }
  }

  /* header */

  .root > header {
    background: #F7F7F7;
    padding: 10px 20px;
    > h1 {
      font-size: 24pt;
      font-family: $main-font-family;
      margin: 0;
      font-weight: normal;
      color: #444;
    }
    .reader-nav {
      float: right;
      font-family: $widget-font-family;
      color: #999;
      a {
        text-decoration: none;
        color: inherit;
        cursor: pointer;
        &:hover {
          color: #000;
        }
      }
    }
  }

  /* main column */

  .main {
    font-family: $main-font-family;
    height: 500px;
    margin: 20px 50px;
    > p:first-of-type {
      margin-top: 0;
    }
  }

  /* text */

  #text {
    clear: both;
    word-spacing: 0.3em;
    line-height: 1.6;
    color: #333;
  }

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
  /* widgets */

  .widget {
    margin-bottom: 10px;
    font-family: $widget-font-family;
    color: #666;
    transition: color 0.2s ease-in-out, opacity 0.5s ease-in-out;
    background: #F7F7F7;
    font-size: 9pt;
    > header {
      cursor: pointer;
      background: #EEE;
      transition: background 0.2s ease-in-out, opacity 0.5s ease-in-out;
      padding: 5px 10px;
      font-weight: bold;
      .summary {
        float: right;
        font-weight: normal;
      }
    }
    > section {
      padding: 10px 10px;
      ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
      }
    }
    &:hover {
      color: #000;
      > header {
        background: #DDD;
      }
    }
  }

  /* pagination */

  div.page-nav-1 {

    display: flex;
    justify-content: space-between;

    overflow: auto;

    font-family: $widget-font-family;

    > div {
      &.prev {
        width: 30px;  // fix width so takes up space even without link
        float: left;
        text-align: left;
      }
      &.next {
        width: 30px;  // fix width so takes up space even without link
        float: right;
        text-align: right;
      }
      line-height: 21pt;
    }

    .title {
      text-align: center;
    }

    a {
      font-weight: bold;
      font-size: 20pt;
      text-decoration: none;
      color: #999;
      cursor: pointer;
    }

    a:hover {
      color: #000;
    }
  }
</style>
