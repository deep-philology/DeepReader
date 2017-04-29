<template>
  <widget>
    <span slot="header">Book Info</span>
    <span slot="summary">{{ $parent.book.name }}</span>
    <div slot="body">
      <b>{{ $parent.book.name }}</b>:
      <nuxt-link :to="$parent.resourceLink($parent.query, $parent.book.first_paragraph)">first paragraph</nuxt-link>
      &bull;
      <nuxt-link :to="$parent.resourceLink($parent.query, $parent.book.first_sentence)">first sentence</nuxt-link>
      &bull;
      <nuxt-link :to="$parent.resourceLink($parent.query, $parent.book.first_verse)">first verse</nuxt-link>
    </div>
  </widget>
</template>

<script>
  import Widget from '~components/Widget.vue'

  export default {
    components: {
      Widget
    }
  }
</script>

<style lang="scss" scoped>
  a {
    color: inherit;
    text-decoration: none;
    &:hover {
      color: #666;
    }
  }
</style>
