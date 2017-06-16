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
  .click {
    color: inherit;
    text-decoration: none;
    cursor: pointer;
    &:hover {
      color: #666;
    }
  }
  .textSize-small {
    font-family: $main-font-family;
    font-size: 14pt;
  }
  .textSize-normal {
    font-family: $main-font-family;
    font-size: 16pt;
  }
  .textSize-large {
    font-family: $main-font-family;
    font-size: 20pt;
  }
</style>

<style lang="scss">
  #text {
    &.textSize-small {
      font-size: 14pt;
    }
    &.textSize-normal {
      font-size: 16pt;
    }
    &.textSize-large {
      font-size: 20pt;
    }
  }
</style>
