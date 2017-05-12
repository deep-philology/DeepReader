<template>
  <div class="page-nav-1">
    <div class="prev"><nuxt-link v-if="prev" :to="prev">&lt;</nuxt-link></div>
    <div class="title">{{ title }}</div>
    <div class="next"><nuxt-link v-if="next" :to="next">&gt;</nuxt-link></div>
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
