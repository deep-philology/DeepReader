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
    created() {
      this.normalText();
    },
    methods: {
      smallerText() {
        this.$store.commit('setTextClass', { textSize: 'small' });
      },
      normalText() {
        this.$store.commit('setTextClass', { textSize: 'normal' });
      },
      largerText() {
        this.$store.commit('setTextClass', { textSize: 'large' });
      },
    },
    components: {
      Widget,
    },
  };
</script>

<style lang="scss" scoped>
  .textSize-small {
    font-family: $main-font-family;
    font-size: $main-text-small-size;
  }
  .textSize-normal {
    font-family: $main-font-family;
    font-size: $main-text-normal-size;
  }
  .textSize-large {
    font-family: $main-font-family;
    font-size: $main-text-large-size;
  }
</style>

<style lang="scss">
  #text {
    &.textSize-small {
      font-size: $main-text-small-size;
    }
    &.textSize-normal {
      font-size: $main-text-normal-size;
    }
    &.textSize-large {
      font-size: $main-text-large-size;
    }
  }
</style>
