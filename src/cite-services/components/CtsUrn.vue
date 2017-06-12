<template>
  <widget>
    <span slot="header">CTS URN</span>
    <div slot="body">
      {{ $route.query.urn }}
    </div>
  </widget>
</template>

<script>
  import Widget from '@/components/Widget';

  export default {
    components: {
      Widget,
    },
  };
</script>
