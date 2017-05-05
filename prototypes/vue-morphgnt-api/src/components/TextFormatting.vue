<template>
  <widget>
    <span slot="header">Text Formatting</span>
    <div slot="body">
      <div class="click" @click="smallerText">Smaller Text</div>
      <div class="click" @click="normalText">Normal Text</div>
      <div class="click" @click="largerText">Larger Text</div>
    </div>
  </widget>
</template>

<script>
  import Widget from '@/components/Widget';

  export default {
    methods: {
      smallerText() {
        this.$store.commit('setTextSize', '14pt');
      },
      normalText() {
        this.$store.commit('setTextSize', '16pt');
      },
      largerText() {
        this.$store.commit('setTextSize', '20pt');
      },
    },
    components: {
      Widget,
    },
  };
</script>

<style lang="scss" scoped>
  div.click {
    color: inherit;
    text-decoration: none;
    cursor: pointer;
    &:hover {
      color: #666;
    }
  }
</style>
