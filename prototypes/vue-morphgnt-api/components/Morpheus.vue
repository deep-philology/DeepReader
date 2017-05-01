<template>
  <widget>
    <span slot="header">Morpheus</span>
    <span slot="summary" class="word-info-summary">
      {{ word }}
    </span>
    <div slot="body" class="word-info-body">
      {{ word }}
    </div>
  </widget>
</template>

<script>
  import axios from 'axios'
  import Widget from '~components/Widget.vue'

  export default {
    mounted () {
      this.$parent.$on('word-select', (word) => {
        this.word = word
        const url = `http://services.perseids.org/bsp/morphologyservice/analysis/word?word=${word.word}&lang=grc&engine=morpheusgrc`
        axios.get(url).then((response) => {
          this.word = response.data
        })
      })
    },
    data () {
      return {
        word: ''
      }
    },
    components: {
      Widget
    }
  }
</script>

<style lang="scss">
</style>
