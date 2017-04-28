<template>
  <div class="widget">
    <header @click.prevent="toggle">Word Info</header>
    <section v-if="open">
      <div class="norm">{{ word.norm }}</div>

      <span class="pos">{{ word.pos }}</span>
      <span v-if="word.mood">.</span>
      {{ word.tense }}{{ word.voice }}{{ word.mood }}
      <span v-if="word.number">.</span>
      {{ word.person }}{{ word.case }}{{ word.number }}{{ word.gender }}

      <div class="lemma">{{ word.lemma }}</div>
    </section>
  </div>
</template>

<script>
export default {
  created () {
    this.$parent.$on('word-select', (word) => {
      this.word = word
    })
  },
  data () {
    return {
      open: true,
      word: {}
    }
  },
  methods: {
    toggle () {
      this.open = !this.open
    }
  }
}
</script>

<style lang="scss" scoped>
  header {
    cursor: pointer;
  }
  section {
    .norm {
      font-size: 150%;
      font-family: "Skolar";
      font-weight: bold;
    }
  }
</style>
