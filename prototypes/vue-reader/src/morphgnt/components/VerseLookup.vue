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
  import morphgnt from '@/morphgnt';
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
        morphgnt.verseLookup(this.verse)
          .then((verseId) => {
            this.verse = '';
            this.$router.push(this.$parent.passageLink(this.$parent.query, verseId));
          })
          .catch((err) => {
            this.error = err;
          });
      },
    },
    components: {
      Widget,
    },
  };
</script>
