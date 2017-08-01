<template>
  <div>
    <h2>
      Keyword in Context
      <input class="keyword-input" v-model.trim.lazy="word">
    </h2>
    <div>
      <table>
        <tr v-for="result in results">
          <td class="pre">{{ result.pre }}</td>
          <td class="keyword">{{ result.keyword }}</td>
          <td class="post">{{ result.post }}</td>
          <td class="ref">
            <router-link class="click"
              :to="{ name: 'MorphGNTReader', query: { passage: result.verse_id } }"
            >{{ result.title }}</router-link>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import Widget from '@/components/Widget';
import morphgnt from '@/morphgnt';

export default {
  data() {
    return {
      results: null,
    };
  },
  created() {
    this.fetchData();
  },
  computed: {
    word() {
      return this.$route.query.word;
    },
  },
  watch: {
    word: 'fetchData',
  },
  methods: {
    fetchData() {
      morphgnt.kwic(this.word).then((results) => {
        this.results = results;
      });
    },
  },
  components: {
    Widget,
  },
};
</script>

<style lang="scss">
  .keyword-input {
    float: right;
    font-size: 18px;
    font-family: $main-font-family;
  }
  table {
    width: 100%;
    .pre {
      text-align: right;
      white-space: nowrap;
    }
    .keyword {
      white-space: nowrap;
      font-weight: bold;
      text-align: left;
    }
    .post {
      text-align: left;
      white-space: nowrap;
    }
    .ref {
      white-space: nowrap;
      text-align: left;
      color: $text-milestone-color;
      font-family: $widget-font-family;
      font-size: 70%;
      padding-left: 2em;
    }
  }
</style>
