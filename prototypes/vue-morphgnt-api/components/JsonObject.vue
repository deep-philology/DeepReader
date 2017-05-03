<template>
  <div>
    <div v-for="value,key in obj">
      <b>{{ key }}</b>:
      <span v-if="typeof(value) === 'string'">{{ value }}</span>
      <div v-else class="sublist">
        <div v-for="subvalue,subkey in value">
          <b>{{ subkey }}</b>: {{ subvalue }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    props: [
      'obj'
    ]
  }
</script>

<style lang="scss" scoped>
  .sublist {
    margin-left: 1em;
  }
</style>
