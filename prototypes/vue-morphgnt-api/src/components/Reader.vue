<template>
  <div class="root">
    <header>
      <h1>Header Text</h1>
    </header>
    <div class="grid-wrapper">
      <div class="left">
        <book-select :books="books"></book-select>
        <book-info v-if="book"></book-info>
      </div>

      <div class="main">
        <template v-if="book">

          <pagination :prev="resourceLink(query, text.prev)" :next="resourceLink(query, text.next)" :title="book.name"></pagination>

          <div id="text">
            <p><span class="word" v-for="word in text.words" @click="handleWordSelect(word)">{{ word.text }} </span></p>
          </div>

          <pagination :prev="resourceLink(query, text.prev)" :next="resourceLink(query, text.next)" :title="book.name"></pagination>

        </template>

      </div>
      <div class="right">
        <word-info></word-info>
        <word-info-list></word-info-list>
        <morpheus></morpheus>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Pagination from '@/components/Pagination';
import BookSelect from '@/components/BookSelect';
import WordInfo from '@/components/WordInfo';
import WordInfoList from '@/components/WordInfoList';
import BookInfo from '@/components/BookInfo';
import Morpheus from '@/components/Morpheus';

const morphgnt = {
  apiRoot: 'https://api.morphgnt.org',
  async resource(path) {
    const { data: resource } = await axios.get(`${this.apiRoot}${path}`);
    return resource;
  },
  async books() {
    const { books } = await this.resource('/v0/root.json');
    return books;
  },
};

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
      text: {},
    };
  },
  watch: {
    $route: 'fetchData',
  },
  methods: {
    fetchData() {
      this.asyncData({ query: this.$route.query }).then(({ query, books, book, text }) => {
        this.query = query;
        this.books = books;
        this.book = book;
        this.text = text;
      });
    },
    async asyncData({ query }) {
      let text = {};
      const books = await morphgnt.books();
      if (query.book) {
        const book = await morphgnt.resource(query.book);
        if (query.resource) {
          text = await morphgnt.resource(query.resource);
        } else {
          text = await morphgnt.resource(book.first_paragraph);
        }
        return { query, books, book, text };
      }
      return { query, books, text };
    },
    renderText(path) {
      morphgnt.resource(path).then((resource) => {
        this.text = resource;
      });
    },
    resourceLink(query, resource) {
      if (resource) {
        return {
          query: Object.assign({}, query, { resource }),
        };
      }
      return {};
    },
    handleKeyUp(e) {
      if (e.key === 'ArrowLeft') {
        if (this.text.prev) {
          this.$router.push(this.resourceLink(this.query, this.text.prev));
        }
      } else if (e.key === 'ArrowRight') {
        if (this.text.next) {
          this.$router.push(this.resourceLink(this.query, this.text.next));
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
    font-size: 20pt;
    line-height: 1.6;
    word-spacing: 0.3em;
    color: #333;
    .word {
      cursor: pointer;
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
