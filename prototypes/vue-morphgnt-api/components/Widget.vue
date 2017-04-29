<template>
  <div class="widget">
    <header @click.prevent="toggle">
      <span class="summary" v-if="!open"><slot name="summary">summary</slot></span>
      <slot name="header">header</slot>
    </header>
    <section v-if="open">
      <slot name="body">body</slot>
    </section>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        open: true
      }
    },
    methods: {
      toggle () {
        this.open = !this.open
      }
    }
  }
</script>
