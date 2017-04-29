<template>
  <widget>
    <span slot="header">Word Info</span>
    <span slot="summary">
      <span class="norm">{{ word.norm }}</span>
      &nbsp;
      <span class="pos">{{ word.pos }}</span>
      <span v-if="word.mood">.</span>
      {{ word.tense }}{{ word.voice }}{{ word.mood }}
      <span v-if="word.number">.</span>
      {{ word.person }}{{ word.case }}{{ word.number }}{{ word.gender }}
      &nbsp;
      <span class="lemma">{{ word.lemma }}</span></span>
    </span>
    <div slot="body">
      <div class="norm">{{ word.norm }}</div>

      <span class="pos">{{ word.pos }}</span>
      <span v-if="word.mood">.</span>
      {{ word.tense }}{{ word.voice }}{{ word.mood }}
      <span v-if="word.number">.</span>
      {{ word.person }}{{ word.case }}{{ word.number }}{{ word.gender }}

      <div class="lemma">{{ word.lemma }}</div>
    </div>
  </widget>
</template>

<script>
  import Widget from '~components/Widget.vue'

  export default {
    created () {
      this.$parent.$on('word-select', (word) => {
        this.word = word
      })
    },
    data () {
      return {
        word: {}
      }
    },
    components: {
      Widget
    }
  }
</script>

<style lang="scss" scoped>
  section {
    .norm {
      font-size: 150%;
      font-family: "Skolar";
      font-weight: bold;
    }
    .lemma {
      font-size: 120%;
      font-family: "Skolar";
    }
  }
</style>
