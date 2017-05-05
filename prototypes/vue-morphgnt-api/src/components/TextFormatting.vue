<template>
  <widget>
    <span slot="header">Text Formatting</span>
    <div slot="body">
      <div @click="smallerText">Smaller Text</div>
      <div @click="normalText">Normal Text</div>
      <div @click="largerText">Larger Text</div>
    </div>
  </widget>
</template>

<script>
  import Widget from '@/components/Widget';

  export default {
    methods: {
      smallerText() {
        this.$store.commit('setTextSize', '10pt');
      },
      normalText() {
        this.$store.commit('setTextSize', '20pt');
      },
      largerText() {
        this.$store.commit('setTextSize', '30pt');
      },
    },
    components: {
      Widget,
    },
  };
</script>
