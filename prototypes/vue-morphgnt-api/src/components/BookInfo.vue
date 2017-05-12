<template>
  <widget>
    <span slot="header">Book Info</span>
    <span slot="summary">{{ $parent.book.name }}</span>
    <div slot="body">
      <b>{{ $parent.book.name }}</b>:
      <router-link :to="$parent.passageLink($parent.query, $parent.book.first_paragraph)">first paragraph</router-link>
      &bull;
      <router-link :to="$parent.passageLink($parent.query, $parent.book.first_sentence)">first sentence</router-link>
      &bull;
      <router-link :to="$parent.passageLink($parent.query, $parent.book.first_verse)">first verse</router-link>
    </div>
  </widget>
</template>

<script>
  import Widget from '@/components/Widget';

  export default {
    components: {
      Widget,
    },
  };
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
