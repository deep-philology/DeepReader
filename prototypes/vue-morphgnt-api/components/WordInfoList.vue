<template>
  <widget>
    <span slot="header">Word Info List</span>
    <span slot="summary">[{{ words.length }}]</span>
    <div slot="body" class="word-info-list-body">
      <div v-for="(word, index) in words" class="word">
        <span class="remove" @click="removeWord(index)">remove</span>
        <word-analysis :word="word"></word-analysis>
      </div>
    </div>
  </widget>
</template>

<script>
  import Widget from '~components/Widget.vue'
  import WordAnalysis from '~components/WordAnalysis.vue'

  export default {
    created () {
      this.$parent.$on('word-select2', (word) => {
        this.words.push(word)
      })
    },
    data () {
      return {
        words: []
      }
    },
    methods: {
      removeWord (index) {
        this.words.splice(index, 1)
      }
    },
    components: {
      Widget,
      WordAnalysis
    }
  }
</script>

<style lang="scss">
  .word-info-list-body {
    .word {
      padding: 2px 5px 2px 0;
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
