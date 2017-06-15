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
        this.$store.commit('setTextClass', { colour: false });
      },
      posColour() {
        this.$store.commit('setTextClass', { colour: 'pos' });
      },
      caseColour() {
        this.$store.commit('setTextClass', { colour: 'case' });
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

<style lang="scss">
  #text {
    &.colour-pos {
      .pos-N, .pos-A {
        color: #C00;
      }
      .pos-RA, .pos-RD, .pos-RI, .pos-RP, .pos-RR {
        color: #C50;
      }
      .pos-V {
        color: #00C;
      }
    }
    &.colour-case {
      .case-N {
        color: #C00;
      }
      .case-G {
        color: #9C6;
      }
      .case-D {
        color: #6CC;
      }
      .case-A {
        color: #FC0;
      }
    }
  }
</style>
