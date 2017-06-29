<template>
  <div class="root">
    <header>
      <div class="reader-nav">
        <router-link to="cts">CTS API (Perseids)</router-link>
        &bull;
        <router-link to="cite-services">cite-services</router-link>
        &bull;
        <router-link to="morphgnt">MorphGNT API</router-link>
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
import Morpheus from '@/widgets/Morpheus';
import TextFormatting from '@/widgets/TextFormatting';
import BookmarkList from '@/widgets/BookmarkList';

import morphgnt from '@/morphgnt';
import BookSelect from '@/morphgnt/widgets/BookSelect';
import WordInfo from '@/morphgnt/widgets/WordInfo';
import BookInfo from '@/morphgnt/widgets/BookInfo';
import VerseLookup from '@/morphgnt/widgets/VerseLookup';
import Interlinear from '@/morphgnt/widgets/Interlinear';
import TextColouring from '@/morphgnt/widgets/TextColouring';
import Frequency from '@/morphgnt/widgets/Frequency';
import Kwic from '@/morphgnt/widgets/Kwic';

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
