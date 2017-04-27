<template>
  <div class="page-nav-1">
    <div class="prev"><a v-if="prev" v-on:click="$emit('page-change', prev)">&lt;</a></div>
    <div class="title">{{ title }}</div>
    <div class="next"><a v-if="next" v-on:click="$emit('page-change', next)">&gt;</a></div>
  </div>
</template>

<script>
export default {
  props: [
    'prev',
    'next',
    'title'
  ]
}
</script>
