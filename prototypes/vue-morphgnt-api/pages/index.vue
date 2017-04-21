<template>
  <div class="root">
    <header>
      <h1>Header Text</h1>
    </header>
    <div class="grid-wrapper">
      <div class="left"></div>
      <div class="main">

        <pagination :prev="text.prev" :next="text.next" v-on:page-change="renderText"></pagination>

        <div id="text">
          <p><span v-for="word in text.words">{{ word.text }} </span></p>
        </div>

        <pagination :prev="text.prev" :next="text.next" v-on:page-change="renderText"></pagination>

      </div>
      <div class="right"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Pagination from '~components/Pagination.vue'

let morphgnt = {
  apiRoot: 'https://api.morphgnt.org',
  async book (name) {
    let { data: book } = await axios.get(`${this.apiRoot}/v0/book/${name}.json`)
    return book
  },
  async resource (path) {
    let { data: resource } = await axios.get(`${this.apiRoot}${path}`)
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
    let book = await morphgnt.book('Matt')
    return { text: await morphgnt.resource(book.first_paragraph) }
  },
  methods: {
    renderText (path) {
      morphgnt.resource(path).then((resource) => {
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
    margin: 20px 0;
    overflow: auto;

    font-family: $widget-font-family;

    a {
      font-weight: bold;
      text-decoration: none;
      padding: 5px 10px;
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
