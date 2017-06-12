<template>
  <widget>
    <span slot="header">Frequency</span>
    <div slot="body">
      <div class="click" @click="toggleFrequency">Toggle</div>
      {{ output }}
    </div>
  </widget>
</template>

<script>
  import { mapGetters } from 'vuex';
  import morphgnt from '@/morphgnt';
  import Widget from '@/components/Widget';

  export default {
    computed: mapGetters(['passage']),
    data() {
      return { output: null };
    },
    methods: {
      toggleFrequency() {
        const input = [];
        this.passage.words.forEach((word, index) => {
          input.push({ id: `w${index}`, lemma: word.lemma });
        });
        morphgnt.frequency(input).then((output) => {
          output.forEach((item) => {
            const c = `freq-${Math.round(Math.log(item.count))}`;
            document.getElementById(item.id).classList.add(c);
          });
        });
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
