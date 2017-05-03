<template>
  <div>
    <div class="norm" @click="handleNormSelect(word)">{{ word.norm }}&nbsp;</div>
    <div class="analysis">
      <span class="pos">{{ word.pos }}</span>
      <span v-if="word.mood">.{{ word.tense }}{{ word.voice }}{{ word.mood }}</span>
      <span v-if="word.number">.{{ word.person }}{{ word.case }}{{ word.number }}{{ word.gender }}</span>
    </div>
    <div class="lemma">{{ word.lemma }}</div>
  </div>
</template>

<script>
  export default {
    props: [
      'word'
    ],
    methods: {
      handleNormSelect (word) {
        this.$parent.$parent.$parent.$emit('word-select', word)
      }
    }
  }
</script>

<style lang="scss" scoped>
  .norm {
    cursor: pointer;
  }
</style>
