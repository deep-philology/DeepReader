<template>
  <widget>
    <span slot="header">Book Info</span>
    <span slot="summary">{{ book.name }}</span>
    <div slot="body">
      <b>{{ book.name }}</b>:
      <router-link class="click" :to="$parent.passageLink(book.first_paragraph)">first paragraph</router-link>
      &bull;
      <router-link class="click" :to="$parent.passageLink(book.first_sentence)">first sentence</router-link>
      &bull;
      <router-link class="click" :to="$parent.passageLink(book.first_verse)">first verse</router-link>
    </div>
  </widget>
</template>

<script>
  import { mapState } from 'vuex';
  import Widget from '@/components/Widget';

  export default {
    computed: {
      ...mapState(['book']),
    },
    components: {
      Widget,
    },
  };
</script>
