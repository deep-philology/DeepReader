<template>
  <widget>
    <span slot="header">Word Info</span>
    <span slot="summary" class="word-info-summary">
      <word-analysis :word="word"></word-analysis>
    </span>
    <div slot="body">
      <div class="word-info-body" v-if="word.norm">
        <word-analysis :word="word"></word-analysis>
      </div>
      <div class="word-info-list-body" v-if="words.length > 0">
        <div v-for="(word, index) in words" class="word">
          <span class="remove" @click="removeWord(index)">remove</span>
          <word-analysis :word="word"></word-analysis>
        </div>
      </div>
    </div>
  </widget>
</template>

<script>
  import Widget from '@/components/Widget';
  import WordAnalysis from '@/morphgnt/components/WordAnalysis';

  export default {
    created() {
      this.$parent.$on('word-select', (word) => {
        this.word = word;
      });
      this.$parent.$on('word-select2', (word) => {
        this.words.push(word);
      });
    },
    data() {
      return {
        word: {},
        words: [],
      };
    },
    methods: {
      removeWord(index) {
        this.words.splice(index, 1);
      },
    },
    components: {
      Widget,
      WordAnalysis,
    },
  };
</script>

<style lang="scss">
  .word-info-summary {
    .norm, .lemma {
      font-family: "Skolar";
      font-size: 120%;
    }
    .norm, .lemma, .analysis {
      display: inline;
      padding-left: 0.5em;
    }
  }
  .word-info-body {
    .norm {
      font-family: "Skolar";
      font-size: 150%;
      font-weight: bold;
    }
    .lemma {
      font-size: 120%;
      font-family: "Skolar";
    }
  }
  .word-info-list-body {
    border-top: 1px solid #CCC;
    margin-top: 10px;
    padding-top: 5px;
    .word {
      padding: 1px 0;
      .remove {
        color: transparent;
        float: right;
        cursor: pointer;
      }
      &:hover {
        .remove {
          transition: color 0.2s ease-in-out;
          color: inherit;
          &:hover {
            color: #C00;
          }
        }
      }
    }
    .norm, .lemma {
      font-family: "Skolar";
      font-size: 120%;
    }
    .norm, .lemma, .analysis {
      display: inline;
      padding-right: 0.5em;
    }
    .norm {
      font-weight: bold;
    }
  }
</style>
