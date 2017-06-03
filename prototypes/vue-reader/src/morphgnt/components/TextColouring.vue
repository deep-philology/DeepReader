<template>
  <widget>
    <span slot="header">Text Colouring</span>
    <div slot="body">
      Colour:
      <span class="click" @click="noColour">none</span>
      <span class="click" @click="posColour">POS</span>
      <span class="click" @click="caseColour">case</span>
    </div>
  </widget>
</template>

<script>
  import Widget from '@/components/Widget';

  export default {
    methods: {
      noColour() {
        this.$store.commit('setColour', null);
      },
      posColour() {
        this.$store.commit('setColour', 'pos');
      },
      caseColour() {
        this.$store.commit('setColour', 'case');
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
