<template>
  <widget>
    <span slot="header">Word Info</span>
    <span slot="summary" class="word-info-summary">
      <word-analysis :word="word"></word-analysis>
    </span>
    <div slot="body" class="word-info-body">
      <word-analysis :word="word"></word-analysis>
    </div>
  </widget>
</template>

<script>
  import Widget from '@/components/Widget';
  import WordAnalysis from '@/components/WordAnalysis';

  export default {
    created() {
      this.$parent.$on('word-select', (word) => {
        this.word = word;
      });
    },
    data() {
      return {
        word: {},
      };
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
</style>
