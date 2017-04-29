<template>
  <widget>
    <span slot="header">Book Select</span>
    <div slot="body">
      <ul>
        <li v-for="book in books"><nuxt-link :to="{ query: {book: book['@id']} }">{{ book.name }}</nuxt-link></li>
      </ul>
    </div>
  </widget>
</template>

<script>
  import Widget from '~components/Widget.vue'

  export default {
    props: [
      'books'
    ],
    components: {
      Widget
    }
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
