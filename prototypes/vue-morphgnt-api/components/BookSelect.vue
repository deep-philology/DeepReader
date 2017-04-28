<template>
  <div class="widget">
    <header @click.prevent="toggle">Book</header>
    <section v-if="open">
      <ul>
        <li v-for="book in books"><nuxt-link :to="{ query: {book: book['@id']} }">{{ book.name }}</nuxt-link></li>
      </ul>
    </section>
  </div>
</template>

<script>
export default {
  data () {
    return {
      open: true
    }
  },
  props: [
    'books'
  ],
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
