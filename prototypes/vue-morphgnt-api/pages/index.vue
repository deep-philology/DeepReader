<template>
  <div class="root">
    <header>
      <h1>Header Text</h1>
    </header>
    <div class="grid-wrapper">
      <div class="left"></div>
      <div class="main">
        <div id="text">
          <p><span v-for="word in paragraph.words">{{ word.text }} </span></p>
        </div>
        <a v-if="paragraph.prev" v-on:click="renderParagraph(paragraph.prev)">prev</a> |
        <a v-if="paragraph.next" v-on:click="renderParagraph(paragraph.next)">next</a>
      </div>
      <div class="right"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

let morphgnt = {
  apiRoot: 'http://api.morphgnt.org',
  async book (name) {
    let { data: book } = await axios.get(`${this.apiRoot}/v0/book/${name}.json`)
    return book
  },
  async paragraph (path) {
    let { data: paragraph } = await axios.get(`${this.apiRoot}${path}`)
    return paragraph
  }
}

export default {
  data () {
    return {
      paragraph: {}
    }
  },
  async asyncData () {
    let book = await morphgnt.book('Matt')
    return { paragraph: await morphgnt.paragraph(book.first_paragraph) }
  },
  methods: {
    renderParagraph (path) {
      morphgnt.paragraph(path).then((paragraph) => {
        this.paragraph = paragraph
      })
    }
  }
}
</script>

<style lang="scss">

  /* variables */

  $main-font-family: "PT Serif";
  $widget-font-family: "PT Sans";

  /* hover opacity */

  .widget, .root > header {
    opacity: 0;
    transition: opacity 0.5s ease-in-out;
  }
  body:hover .widget, body:hover .root > header {
    opacity: 1;
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
    font-size: 16pt;
    line-height: 1.5;
    word-spacing: normal;
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
</style>
