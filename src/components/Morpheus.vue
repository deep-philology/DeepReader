<template>
  <widget>
    <span slot="header">Morpheus (Raw Response)</span>
    <span slot="summary">
      {{ word.word }}
    </span>
    <div slot="body" v-if="morphBody">
      <json-object :obj="morphBody"></json-object>
    </div>
  </widget>
</template>

<script>
  import fetch from 'universal-fetch';
  import Widget from '@/components/Widget';
  import JsonObject from '@/components/JsonObject';

  export default {
    mounted() {
      this.$parent.$on('word-select', (word) => {
        this.word = word;
        const url = `http://services.perseids.org/bsp/morphologyservice/analysis/word?word=${word.word}&lang=grc&engine=morpheusgrc`;
        const headers = new Headers({
          Accept: 'application/json',
        });
        fetch(url, { method: 'GET', headers }).then((resp) => {
          resp.json().then((data) => {
            this.morphBody = data.RDF.Annotation.Body;
          });
        });
      });
    },
    data() {
      return {
        word: '',
        morphBody: null,
      };
    },
    components: {
      Widget,
      JsonObject,
    },
  };
</script>
