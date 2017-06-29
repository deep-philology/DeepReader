<template>
  <widget>
    <span slot="header">Interlinear</span>
    <div slot="body">
      <div class="click" @click="toggleInterlinear">Toggle</div>
    </div>
  </widget>
</template>

<script>
  import Widget from '@/components/Widget';

  export default {
    methods: {
      toggleInterlinear() {
        this.$store.commit('toggleInterlinear');
      },
    },
    components: {
      Widget,
    },
  };
</script>
