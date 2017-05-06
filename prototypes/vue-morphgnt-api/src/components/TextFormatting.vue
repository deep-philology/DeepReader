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
  div.click {
    color: inherit;
    text-decoration: none;
    cursor: pointer;
    &:hover {
      color: #666;
    }
  }
</style>
