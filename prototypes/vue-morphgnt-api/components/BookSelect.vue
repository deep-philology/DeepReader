<template>
  <div class="widget">
    <header>Book</header>
    <section>
      <ul>
        <li v-for="book in books"><nuxt-link :to="{ query: {book: book['@id']} }">{{ book.name }}</nuxt-link></li>
      </ul>
    </section>
  </div>
</template>

<script>
export default {
  props: [
    'books'
  ]
}
</script>

<style lang="scss" scoped>
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
