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
      <h1>DeepReader (MorphGNT)</h1>
    </header>
    <div class="grid-wrapper">
      <div class="left">
        <book-select :books="books"></book-select>
        <book-info v-if="book"></book-info>
        <verse-lookup></verse-lookup>
        <bookmark-list v-if="user"></bookmark-list>
      </div>

      <div class="main">
        <passage :linker="passageLink"></passage>
      </div>

      <div class="right">
        <text-formatting></text-formatting>
        <text-colouring></text-colouring>
        <interlinear></interlinear>
        <frequency></frequency>
        <word-info></word-info>
        <morpheus></morpheus>
        <kwic></kwic>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import Passage from '@/components/Passage';
import Morpheus from '@/components/Morpheus';
import TextFormatting from '@/components/TextFormatting';
import BookmarkList from '@/components/BookmarkList';

import morphgnt from '@/morphgnt';
import BookSelect from '@/morphgnt/components/BookSelect';
import WordInfo from '@/morphgnt/components/WordInfo';
import BookInfo from '@/morphgnt/components/BookInfo';
import VerseLookup from '@/morphgnt/components/VerseLookup';
import Interlinear from '@/morphgnt/components/Interlinear';
import TextColouring from '@/morphgnt/components/TextColouring';
import Frequency from '@/morphgnt/components/Frequency';
import Kwic from '@/morphgnt/components/Kwic';

export default {
  name: 'reader',
  created() {
    this.$store.commit('setReader', { book: null, passage: null });
    this.fetchData();
  },
  data() {
    return {
      query: {},
      books: [],
    };
  },
  computed: {
    ...mapState(['user', 'book']),
  },
  watch: {
    $route: 'fetchData',
  },
  methods: {
    fetchData() {
      this.asyncData({ query: this.$route.query }).then(({ query, books, book, passage }) => {
        if (book && !passage) {
          this.$router.push(this.passageLink(book.first_paragraph));
        } else {
          this.query = query;
          this.books = books;
          this.$store.commit('setReader', { book, passage });
        }
      });
    },
    async asyncData({ query }) {
      let book = null;
      let passage = null;
      const books = await morphgnt.books();
      if (query.passage) {
        const {
          prev,
          next,
          title,
          words,
          ...p
        } = await morphgnt.resource(query.passage);
        passage = {
          prev,
          next,
          title,
          words: words.map(word => ({
            id: word['@id'].slice(-16, -5),
            classes: [
              `pos-${word.pos}`,
              `case-${word.case}`,
            ],
            text: word.text,
            // @@@ move to annotations API
            norm: word.norm,
            lemma: word.lemma,
            mood: word.mood,
            tense: word.tense,
            voice: word.voice,
            number: word.number,
            person: word.person,
            pos: word.pos,
            case: word.case,
            word: word.word,
            gender: word.gender,
          })),
        };
        book = await morphgnt.resource(p.book);
      } else if (query.book) {
        book = await morphgnt.resource(query.book);
      }
      return { query, books, book, passage };
    },
    passageLink(passage) {
      const { query } = this;
      if (passage) {
        delete query.book;
        return {
          query: Object.assign({}, query, { passage }),
        };
      }
      return null;
    },
  },
  components: {
    BookSelect,
    WordInfo,
    BookInfo,
    Morpheus,
    BookmarkList,
    VerseLookup,
    Passage,
    TextFormatting,
    Interlinear,
    TextColouring,
    Frequency,
    Kwic,
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
