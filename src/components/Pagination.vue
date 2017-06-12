<template>
  <div class="page-nav-1">
    <div class="prev"><router-link v-if="prev" :to="prev">&lt;</router-link></div>
    <div class="title">{{ title }}</div>
    <div class="next"><router-link v-if="next" :to="next">&gt;</router-link></div>
  </div>
</template>

<script>
  export default {
    props: [
      'prev',
      'next',
      'title',
    ],
  };
</script>
