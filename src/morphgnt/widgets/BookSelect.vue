<template>
  <widget>
    <span slot="header">Book Select</span>
    <div slot="body">
      <ul>
        <li v-for="book in books"><router-link class="click" :to="{query: {book: book['@id']}}">{{ book.name }}</router-link></li>
      </ul>
    </div>
  </widget>
</template>

<script>
  import Widget from '@/components/Widget';

  export default {
    props: [
      'books',
    ],
    components: {
      Widget,
    },
  };
</script>
