<template>
  <widget>
    <span slot="header">Verse Lookup</span>
    <div slot="body">
      <input type="text" v-model="verse" v-on:keyup="handleKeyUp" />
      {{ error }}
    </div>
  </widget>
</template>

<script>
  import axios from 'axios';
  import Widget from '@/components/Widget';

  export default {
    data() {
      return {
        verse: '',
        error: '',
      };
    },
    methods: {
      handleKeyUp(e) {
        if (e.key === 'Enter') {
          this.error = '';
          this.fetchVerse();
        }
      },
      fetchVerse() {
        const url = `http://localhost:8000/v0/verse-lookup/?${this.verse}`;
        axios.get(url, { validateStatus: null }).then((response) => {
          if (response.status === 400) {
            this.error = response.data.message;
          } else {
            this.verse = '';
            this.$router.push(this.$parent.passageLink(this.$parent.query, response.data.verse_id));
          }
        });
      },
    },
    components: {
      Widget,
    },
  };
</script>
