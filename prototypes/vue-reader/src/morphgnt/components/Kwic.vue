<template>
  <widget>
    <span slot="header">KWIC</span>
    <span slot="summary">
      {{ word.word }}
    </span>
    <div slot="body" v-if="results">
      <table>
        <tr v-for="result in results">
          <td class="pre">{{ result.pre }}</td>
          <td class="keyword">{{ result.keyword }}</td>
          <td class="post">{{ result.post }}</td>
        </tr>
      </table>
    </div>
  </widget>
</template>

<script>
import Widget from '@/components/Widget';
import JsonObject from '@/components/JsonObject';
import morphgnt from '@/morphgnt';

export default {
  mounted() {
    this.$parent.$on('word-select', (word) => {
      this.word = word;
      morphgnt.kwic(word.word).then((results) => {
        this.results = results;
      });
    });
  },
  data() {
    return {
      word: '',
      results: null,
    };
  },
  components: {
    Widget,
    JsonObject,
  },
};
</script>

<style lang="scss">
  table {
    width: 100%;
    .pre {
      text-align: right;
    }
    .keyword {
      white-space: nowrap;
      font-weight: bold;
      text-align: center;
    }
    .post {
      text-align: left;
    }
  }
</style>
