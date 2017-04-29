<template>
  <div>
    <div class="norm">{{ word.norm }}&nbsp;</div>
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
    ]
  }
</script>
