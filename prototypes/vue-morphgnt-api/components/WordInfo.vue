<template>
  <div class="widget">
    <header @click.prevent="toggle">Word Info</header>
    <section v-if="open">
      {{ word }}
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
