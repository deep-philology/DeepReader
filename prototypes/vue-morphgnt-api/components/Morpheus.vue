<template>
  <widget>
    <span slot="header">Morpheus</span>
    <span slot="summary">
      {{ word.word }}
    </span>
    <div slot="body" v-if="morphEntry">
      <json-object :obj="morphEntry.dict"></json-object>
      <div v-if="Array.isArray(morphEntry.infl)">
        <json-object v-for="item,index in morphEntry.infl" class="item" :obj="item"></json-object>
      </div>
      <json-object v-else :obj="morphEntry.infl" class="item"></json-object>
    </div>
  </widget>
</template>

<script>
  import axios from 'axios'
  import Widget from '~components/Widget.vue'
  import JsonObject from '~components/JsonObject.vue'

  export default {
    mounted () {
      this.$parent.$on('word-select', (word) => {
        this.word = word
        const url = `http://services.perseids.org/bsp/morphologyservice/analysis/word?word=${word.word}&lang=grc&engine=morpheusgrc`
        axios.get(url).then((response) => {
          this.morphEntry = response.data.RDF.Annotation.Body.rest.entry
        })
      })
    },
    data () {
      return {
        word: '',
        morphEntry: null
      }
    },
    components: {
      Widget,
      JsonObject
    }
  }
</script>

<style lang="scss" scoped>
  .item {
    margin: 10px 0;
    padding-left: 10px;
    border-left: 2px solid #CCC;
  }
</style>
