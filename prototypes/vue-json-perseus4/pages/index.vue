<template>
  <div class="root">
    <header>
      <h1>Header Text</h1>
    </header>
    <div class="grid-wrapper">
      <div class="left"></div>
      <div class="main">

        <pagination :prev="text.prev" :next="text.next" :title="text.title" v-on:page-change="renderText"></pagination>

        <div id="text" v-html="text.content"></div>

        <pagination :prev="text.prev" :next="text.next" :title="text.title" v-on:page-change="renderText"></pagination>

      </div>
      <div class="right"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Pagination from '~components/Pagination.vue'

let perseus = {
  apiRoot: 'http://localhost:8000',
  async resource (file) {
    let { data: resource } = await axios.get(`${this.apiRoot}/${file}`)
    return resource
  }
}

export default {
  data () {
    return {
      text: {}
    }
  },
  async asyncData () {
    return { text: await perseus.resource('1.json') }
  },
  methods: {
    renderText (path) {
      perseus.resource(path).then((resource) => {
        this.text = resource
      })
    }
  },
  components: {
    Pagination
  }
}
</script>

<style lang="scss">

  /* variables */

  $main-font-family: "Skolar PE";
  $widget-font-family: "PT Sans";

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
    background: #DDD;
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
    font-size: 20pt;
    line-height: 1.6;
    word-spacing: 0.3em;
    color: #333;

    span.section {
      font-family: "Skolar";
      color: #933;
      font-weight: normal;
      font-variant: small-caps;
    }
  }

  /* widgets */

  .widget {
    margin-bottom: 10px;
    font-family: $widget-font-family;
    color: #666;
    background: #F7F7F7;
    font-size: 9pt;
    > header {
      background: #EEE;
      padding: 5px 10px;
      font-weight: bold;
    }
    > section {
      padding: 10px 10px;
    }
  }

  /* pagination */

  div.page-nav-1 {

    display: flex;
    justify-content: space-between;

    margin: 20px 0;
    overflow: auto;

    font-family: $widget-font-family;

    > div.prev, > div.next {
      width: 50px;  // fix width so takes up space even without link
    }

    .title {
      padding: 5px 10px;
      text-align: center;
    }

    a {
      display: inline-block;
      padding: 5px 10px;
      font-weight: bold;
      text-decoration: none;
      background: #EEE;
      color: #666;
      cursor: pointer;

      &.prev {
        float: left;
      }
      &.next {
        float: right;
      }
    }

    a:hover {
      background: #CCC;
    }
  }
</style>
