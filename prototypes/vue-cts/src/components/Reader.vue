<template>
  <div class="root">
    <header>
      <h1><b>LORE</b>: Learner’s Online Reading Environment (CTS)</h1>
    </header>
    <div class="grid-wrapper">
      <div class="left">
        <text-inventory></text-inventory>
        <text-group v-if="ctsTextGroup"></text-group>
        <work v-if="ctsWork"></work>
      </div>

      <div class="main">
        <template v-if="passage">

          <pagination :prev="passageLink(query, passage.prev)" :next="passageLink(query, passage.next)" :title="passage.title"></pagination>

          <div id="text" :class="'textSize-' + this.textSize"></div>

          <pagination :prev="passageLink(query, passage.prev)" :next="passageLink(query, passage.next)" :title="passage.title"></pagination>

        </template>
        <div v-else>
          Nothing here yet.
        </div>


      </div>
      <div class="right">
        <text-formatting></text-formatting>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import xpath from 'xpath';
import fetch from 'universal-fetch';
import Pagination from '@/components/Pagination';
import TextFormatting from '@/components/TextFormatting';
import TextInventory from '@/components/TextInventory';
import TextGroup from '@/components/TextGroup';
import Work from '@/components/Work';

export default {
  name: 'reader',
  created() {
    this.fetchData();
  },
  mounted() {
    window.addEventListener('keyup', this.handleKeyUp);
  },
  beforeDestroy() {
    window.removeEventListener('keyup', this.handleKeyUp);
  },
  data() {
    return {
      query: null,
    };
  },
  computed: mapGetters(['user', 'passage', 'textSize', 'ctsTextGroup', 'ctsWork']),
  watch: {
    $route: 'fetchData',
    passage: 'updateReader',
  },
  methods: {
    updateReader() {
      document.getElementById('text').innerHTML = '';
      document.getElementById('text').appendChild(this.passage.fragment);
    },
    fetchData() {
      this.asyncData({ query: this.$route.query }).then(({ query, passage }) => {
        this.query = query;
        this.$store.commit('setReader', { passage });
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
      const xslDoc = parser.parseFromString(`<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:cts="http://chs.harvard.edu/xmlns/cts" xmlns:tei="http://www.tei-c.org/ns/1.0">
  <xsl:output method="html" />

  <xsl:template match="/">
    <xsl:apply-templates select="//tei:TEI" />
  </xsl:template>

  <xsl:template match="tei:div">
    <div><xsl:apply-templates /></div>
  </xsl:template>

  <xsl:template match="tei:p">
    <p><xsl:apply-templates /></p>
  </xsl:template>

  <xsl:template match="tei:l">
    <div><xsl:apply-templates /> {<xsl:value-of select="@n"/>}</div>
  </xsl:template>

  <xsl:template match="*">
    [<xsl:value-of select="local-name()"/>
      <xsl:for-each select="@*">
        <xsl:text> </xsl:text>
        <xsl:value-of select="name()"/>=<xsl:value-of select="."/>
      </xsl:for-each>]
    <xsl:apply-templates />
    [/<xsl:value-of select ="local-name()"/>]
  </xsl:template>
</xsl:stylesheet>`, 'text/xml');
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
    passageLink(query, urn) {
      if (urn) {
        return {
          query: Object.assign({}, query, { urn }),
        };
      }
      return null;
    },
    handleKeyUp(e) {
      if (e.key === 'ArrowLeft') {
        if (this.passage.prev) {
          this.$router.push(this.passageLink(this.query, this.passage.prev));
        }
      } else if (e.key === 'ArrowRight') {
        if (this.passage.next) {
          this.$router.push(this.passageLink(this.query, this.passage.next));
        }
      }
    },
    handleWordSelect(word) {
      this.$emit('word-select', word);
      this.$emit('word-select2', word);
    },
  },
  components: {
    Pagination,
    TextFormatting,
    TextInventory,
    TextGroup,
    Work,
  },
};
</script>

<style lang="scss">

  /* variables */

  $main-font-family: "Skolar";
  $widget-font-family: "PT Sans", $main-font-family;

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
    &.textSize-small {
      font-size: 14pt;
    }
    &.textSize-normal {
      font-size: 16pt;
    }
    &.textSize-large {
      font-size: 20pt;
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
      .textSize-small {
        font-family: $main-font-family;
        font-size: 14pt;
      }
      .textSize-normal {
        font-family: $main-font-family;
        font-size: 16pt;
      }
      .textSize-large {
        font-family: $main-font-family;
        font-size: 20pt;
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
      line-height: 20pt;
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
