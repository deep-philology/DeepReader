<template>
  <div class="root">
    <header>
      <h1>Header Text</h1>
    </header>
    <div class="grid-wrapper">
      <div class="left"></div>
      <div class="main">
        <div id="text">
          <p><span v-for="word in words">{{ word.text }} </span></p>
        </div>
      </div>
      <div class="right"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  async asyncData () {
    let { data: book } = await axios.get('http://api.morphgnt.org/v0/book/Luke.json')
    let { data: paragraph } = await axios.get('http://api.morphgnt.org' + book.first_paragraph)
    return { words: paragraph.words }
  }
}
</script>

<style lang="scss">
  .root > header {
    background: #DDD;
    padding: 10px 20px;
  }
  .root > header > h1 {
    font-size: 24pt;
    font-family: "PT Serif";
    margin: 0;
    font-weight: normal;
    color: #444;
  }
  .widget, .root > header {
    opacity: 0;
    transition: opacity 0.5s ease-in-out;
  }
  body:hover .widget, body:hover .root > header {
    opacity: 1;
  }
  .grid-wrapper {
    display: grid;
    grid-template-columns: 2fr 6fr 4fr;
    grid-column-gap: 10px;
    margin: 10px;
  }
  .grid-wrapper > * {
    min-width: 200px;
  }
  .main {
    font-family: "PT Serif";
    height: 500px;
    margin: 20px 50px;
  }
  .main > p:first-of-type {
    margin-top: 0;
  }
  .left, .right {
  }
  .widget {
    margin-bottom: 10px;
    font-family: "PT Sans";
    color: #666;
    background: #F7F7F7;
    font-size: 9pt;
  }
  .widget > header {
    background: #EEE;
    padding: 5px 10px;
    font-weight: bold;
  }
  .widget > section {
    padding: 10px 10px;
  }
  #text {
    font-size: 16pt;
    line-height: 1.5;
    word-spacing: normal;
    color: #333;
  }
</style>
