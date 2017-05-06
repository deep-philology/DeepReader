<template>
  <div class="root">
    <header>
      <h1><b>LORE</b>: Learner’s Online Reading Environment</h1>
    </header>
    <div class="grid-wrapper">
      <div class="left">
        <book-select :books="books"></book-select>
        <book-info v-if="book"></book-info>
        <verse-lookup></verse-lookup>
        <bookmark-list v-if="user"></bookmark-list>
      </div>

      <div class="main">
        <template v-if="book">

          <pagination :prev="passageLink(query, passage.prev)" :next="passageLink(query, passage.next)" :title="passage.title"></pagination>

          <div id="text" :class="'textSize-' + this.textSize + (this.colour ? ' colour-' + this.colour : '')">
            <p>
              <div class="word unit" v-for="word in passage.words" @click="handleWordSelect(word)">
                <span class="verse-num" v-if="word['@id'].slice(-8, -5) == '001'">{{ parseInt(word['@id'].slice(-11, -8)) }}</span>
                <span :class="'txt pos-' + word.pos + ' case-' + word.case">{{ word.text }}</span>
                <br><template v-if="interlinear"><span class="gls">
                  <span class="pos">{{ word.pos }}</span><span v-if="word.mood">.{{ word.tense }}{{ word.voice }}{{ word.mood }}</span><span v-if="word.number">.{{ word.person }}{{ word.case }}{{ word.number }}{{ word.gender }}</span>
                  <br>{{ word.lemma }}
                </span></template>
              </div>
            </p>
          </div>

          <pagination :prev="passageLink(query, passage.prev)" :next="passageLink(query, passage.next)" :title="passage.title"></pagination>

        </template>

      </div>
      <div class="right">
        <text-formatting></text-formatting>
        <text-colouring></text-colouring>
        <interlinear></interlinear>
        <word-info></word-info>
        <word-info-list></word-info-list>
        <morpheus></morpheus>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import morphgnt from '@/morphgnt';
import Pagination from '@/components/Pagination';
import BookSelect from '@/components/BookSelect';
import WordInfo from '@/components/WordInfo';
import WordInfoList from '@/components/WordInfoList';
import BookInfo from '@/components/BookInfo';
import Morpheus from '@/components/Morpheus';
import BookmarkList from '@/components/BookmarkList';
import VerseLookup from '@/components/VerseLookup';
import TextFormatting from '@/components/TextFormatting';
import Interlinear from '@/components/Interlinear';
import TextColouring from '@/components/TextColouring';

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
      query: {},
      books: [],
      book: null,
      passage: null,
    };
  },
  computed: mapGetters(['user', 'textSize', 'interlinear', 'colour']),
  watch: {
    $route: 'fetchData',
  },
  methods: {
    fetchData() {
      this.asyncData({ query: this.$route.query }).then(({ query, books, book, passage }) => {
        if (book && !passage) {
          this.$router.push(this.passageLink(query, book.first_paragraph));
        }
        this.query = query;
        this.books = books;
        this.book = book;
        this.passage = passage;
      });
    },
    async asyncData({ query }) {
      let book = null;
      let passage = null;
      const books = await morphgnt.books();
      if (query.passage) {
        passage = await morphgnt.resource(query.passage);
        book = await morphgnt.resource(passage.book);
      } else if (query.book) {
        book = await morphgnt.resource(query.book);
      }
      return { query, books, book, passage };
    },
    renderPassage(path) {
      morphgnt.resource(path).then((resource) => {
        this.passage = resource;
      });
    },
    passageLink(query, passage) {
      if (passage) {
        delete query.book;
        return {
          query: Object.assign({}, query, { passage }),
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
    BookSelect,
    WordInfo,
    WordInfoList,
    BookInfo,
    Morpheus,
    BookmarkList,
    VerseLookup,
    TextFormatting,
    Interlinear,
    TextColouring,
  },
};
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
    color: #333;
    .word {
      cursor: pointer;
      .verse-num {
        color: #999;
        font-family: $widget-font-family;
        font-size: 60%;
      }
    }
    &.textSize-small {
      font-size: 14pt;
    }
    &.textSize-normal {
      font-size: 16pt;
    }
    &.textSize-large {
      font-size: 20pt;
    }

    div.unit {
      display: inline-block;
      margin-bottom: 0.5em;
    }
    .txt {
      display: inline-block;
    }
    .gls {
      display: inline-block;
      font-size: 75%;
      color: gray;
    }

    &.colour-pos {
      .pos-N, .pos-A {
        color: #C00;
      }
      .pos-RA, .pos-RD, .pos-RI, .pos-RP, .pos-RR {
        color: #C50;
      }
      .pos-V {
        color: #00C;
      }
    }
    &.colour-case {
      .case-N {
        color: #C00;
      }
      .case-G {
        color: #9C6;
      }
      .case-D {
        color: #6CC;
      }
      .case-A {
        color: #FC0;
      }
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
