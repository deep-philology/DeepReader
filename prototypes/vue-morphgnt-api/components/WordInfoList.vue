<template>
  <widget>
    <span slot="header">Word Info List</span>
    <span slot="summary">[{{ words.length }}]</span>
    <div slot="body">
      <div v-for="(word, index) in words" class="word">
        <span class="remove" @click="removeWord(index)">remove</span>
        <span class="norm">{{ word.norm }}</span>
        &nbsp;
        <span class="pos">{{ word.pos }}</span>
        <span v-if="word.mood">.</span>
        {{ word.tense }}{{ word.voice }}{{ word.mood }}
        <span v-if="word.number">.</span>
        {{ word.person }}{{ word.case }}{{ word.number }}{{ word.gender }}
        &nbsp;
        <span class="lemma">{{ word.lemma }}</span>
      </div>
    </div>
  </widget>
</template>

<script>
  import Widget from '~components/Widget.vue'

  export default {
    created () {
      this.$parent.$on('word-select', (word) => {
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
      Widget
    }
  }
</script>

<style lang="scss" scoped>
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
  .norm {
    font-weight: bold;
    font-size: 120%;
    font-family: "Skolar";
  }
  .lemma {
    font-size: 120%;
    font-family: "Skolar";
  }
</style>
