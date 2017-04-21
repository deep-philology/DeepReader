<template>
  <div class="page-nav-1">
    <a class="prev" v-if="prev" v-on:click="$emit('page-change', prev)">&lt;</a>
    <a class="next" v-if="next" v-on:click="$emit('page-change', next)">&gt;</a>
  </div>
</template>

<script>
export default {
  props: [
    'prev',
    'next'
  ]
}
</script>
