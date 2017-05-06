<template>
  <widget>
    <span slot="header">Text Formatting</span>
    <div slot="body">
      Size:
      <span class="click textSize-small" @click="smallerText">αβ</span>
      <span class="click textSize-normal" @click="normalText">αβ</span>
      <span class="click textSize-large" @click="largerText">αβ</span>
    </div>
  </widget>
</template>

<script>
  import Widget from '@/components/Widget';

  export default {
    methods: {
      smallerText() {
        this.$store.commit('setTextSize', 'small');
      },
      normalText() {
        this.$store.commit('setTextSize', 'normal');
      },
      largerText() {
        this.$store.commit('setTextSize', 'large');
      },
    },
    components: {
      Widget,
    },
  };
</script>

<style lang="scss" scoped>
  .click {
    color: inherit;
    text-decoration: none;
    cursor: pointer;
    &:hover {
      color: #666;
    }
  }
</style>
