<template>
  <div class="widget">
    <header @click.prevent="toggle"><span v-if="!open">{{ words.length }}</span> Word Info List</header>
    <section v-if="open">
      <div v-for="word in words">
        <span @click="removeWord(word)">x</span> {{ word }}
      </div>
    </section>
  </div>
</template>

<script>
export default {
  created () {
    this.$parent.$on('word-select', (word) => {
      this.words.push(word)
    })
  },
  data () {
    return {
      open: true,
      words: []
    }
  },
  methods: {
    toggle () {
      this.open = !this.open
    },
    removeWord (word) {
      this.words.splice(this.words.indexOf(word), 1)
    }
  }
}
</script>

<style lang="scss" scoped>
  header {
    cursor: pointer;
  }
  a {
    display: block;
    color: inherit;
    text-decoration: none;
    padding: 2px 5px;
    &:hover {
      background: #DDD;
    }
  }
</style>
