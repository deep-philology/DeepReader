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

<style lang="scss" scoped>
  div.page-nav-1 {

    display: flex;
    justify-content: space-between;

    overflow: auto;

    font-family: $widget-font-family;

    > div {
      &.prev {
        width: 30px;  // fix width so takes up space even without link
        float: left;
        text-align: left;
      }
      &.next {
        width: 30px;  // fix width so takes up space even without link
        float: right;
        text-align: right;
      }
      line-height: 21pt;
    }

    .title {
      text-align: center;
    }

    a {
      font-weight: bold;
      font-size: 20pt;
      text-decoration: none;
      color: #999;
      cursor: pointer;
    }

    a:hover {
      color: #000;
    }
  }
</style>
