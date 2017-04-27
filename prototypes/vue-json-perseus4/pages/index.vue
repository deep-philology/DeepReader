<template>
  <div class="root">
    <header>
      <h1>Header Text</h1>
    </header>
    <div class="grid-wrapper">
      <div class="left"></div>
      <div class="main">

        <pagination :prev="resourceLink(query, text.prev)" :next="resourceLink(query, text.next)" :title="text.title"></pagination>

        <div id="text" v-html="text.content"></div>

        <pagination :prev="resourceLink(query, text.prev)" :next="resourceLink(query, text.next)" :title="text.title"></pagination>

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
  created () {
    if (process.BROWSER_BUILD) {
      window.addEventListener('keyup', this.handleKeyUp)
    }
  },
  beforeDestroy () {
    if (process.BROWSER_BUILD) {
      window.removeEventListener('keyup', this.handleKeyUp)
    }
  },
  data () {
    return {
      query: {},
      text: {}
    }
  },
  async asyncData ({ query }) {
    var text = {}
    if (query.resource) {
      text = await perseus.resource(query.resource)
    } else {
      text = await perseus.resource('1.json')
    }
    return { query, text }
  },
  methods: {
    renderText (path) {
      perseus.resource(path).then((resource) => {
        this.text = resource
      })
    },
    resourceLink (query, resource) {
      if (resource) {
        return {
          query: Object.assign({}, query, { resource })
        }
      }
    },
    handleKeyUp (e) {
      if (e.key === 'ArrowLeft') {
        if (this.text.prev) {
          this.$router.push(this.resourceLink(this.query, this.text.prev))
        }
      } else if (e.key === 'ArrowRight') {
        if (this.text.next) {
          this.$router.push(this.resourceLink(this.query, this.text.next))
        }
      }
    }
  },
  components: {
    Pagination
  }
}
</script>

<style lang="scss">

  /* variables */

  $main-font-family: "Skolar";
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
    position: relative;

    span.section {
      font-family: $widget-font-family;
      color: #BBB;
      font-weight: normal;
      vertical-align: super;
      font-size: 70%;
      // position: absolute;
      // left: -30px;
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

    margin: 40px 0;
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
