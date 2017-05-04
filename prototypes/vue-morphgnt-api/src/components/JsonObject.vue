<template>
  <div>
    <div v-for="value,key in obj">
      <b>{{ key }}</b>:
      <span v-if="typeof(value) != 'object'">{{ value }}</span>
      <json-object v-else class="sublist" :obj="value"></json-object>
    </div>
  </div>
</template>

<script>
  import JsonObject from '@/components/JsonObject';

  export default {
    name: 'JsonObject',
    props: [
      'obj',
    ],
    components: {
      JsonObject,
    },
  };
</script>

<style lang="scss" scoped>
  .sublist {
    margin-left: 1em;
  }
</style>
