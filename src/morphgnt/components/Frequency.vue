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
  import { mapState } from 'vuex';
  import morphgnt from '@/morphgnt';
  import Widget from '@/components/Widget';

  export default {
    computed: mapState(['passage']),
    data() {
      return { output: null };
    },
    methods: {
      toggleFrequency() {
        const input = [];
        this.passage.words.forEach((word) => {
          input.push({ id: word.id, lemma: word.lemma });
        });
        morphgnt.frequency(input).then((output) => {
          output.forEach((item) => {
            const c = `freq-${Math.round(Math.log(item.count))}`;
            document.getElementById(item.id).classList.toggle(c);
          });
        });
      },
    },
    components: {
      Widget,
    },
  };
</script>

<style lang="scss">
  #text {
    .freq-0, .freq-1, .freq-2, .freq-3, .freq-4, .freq-5, .freq-6, .freq-7,
    .freq-8, .freq-9, .freq-10 {
      padding: 0.2em 0.3em;
      margin: -0.2em -0.3em;
    }
    .freq-0 {
      background: #6ff;
    }
    .freq-1 {
      background: #6fe;
    }
    .freq-2 {
      background: #7fd;
    }
    .freq-3 {
      background: #8fc;
    }
    .freq-4 {
      background: #9fb;
    }
    .freq-5 {
      background: #afa;
    }
    .freq-6 {
      background: #bf9;
    }
    .freq-7 {
      background: #cf8;
    }
    .freq-8 {
      background: #df7;
    }
    .freq-9 {
      background: #ef6;
    }
    .freq-10 {
      background: #ff5;
    }
  }
</style>
