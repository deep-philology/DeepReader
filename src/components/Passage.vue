<template>
  <div>
    <template v-if="passage">
      <pagination
        :prev="linker(passage.prev)"
        :next="linker(passage.next)"
        :title="passage.title">
      </pagination>
      <div id="text" :class="textClasses" v-fragment="passage.fragment">
        <p>
          <span
            v-for="word in passage.words"
            :key="word.id" :id="word.id"
            :class="['word', ...word.classes]"
            @click="handleWordSelect(word)"
          >
            <span class="verse-num" v-if="word.id.slice(-8, -5) == '001'">{{ parseInt(word.id.slice(-11, -8)) }}</span>
            {{ word.text }}
            <template v-if="interlinear">
              <br>
              <span class="gls">
                <span class="pos">{{ word.pos }}</span>
                <span v-if="word.mood">.{{ word.tense }}{{ word.voice }}{{ word.mood }}</span>
                <span v-if="word.number">.{{ word.person }}{{ word.case }}{{ word.number }}{{ word.gender }}</span>
                <br>
                {{ word.lemma }}
              </span>
            </template>
          </span>
        </p>
      </div>
      <pagination
        :prev="linker(passage.prev)"
        :next="linker(passage.next)"
        :title="passage.title">
      </pagination>
    </template>
    <div v-else>
      <p>
        DeepReader is a highly modular, Vue.js-based online reading
        environment designed for deep reading of texts with integrated
        learning tools.
      </p>
      <p>
        It is particulary intended for the study of classical languages
        such as Ancient Greek but could be applied to any texts with rich
        annotations. What is here is an early prototype using the MorphGNT
        API and the CTS protocol but we plan to support other text services
        as well.
      </p>
      <p>
        If you hover over the reader, you'll see various pluggable widgets
        on the left and right. Those on the left are used to choose what
        passage to read, and those on the right are used to present
        additional information about the passage and its individual words,
        and to control the appearance of the passage.
      </p>
      <p>
        You can expand or collapse any widget by clicking on its title. You
        can use the arrow keys on your keyboard to pagination between
        passages in a work.
      </p>
      <p>
        Each widget is a separate Vue.js component. We are working to make
        it as simple as possible to develop new widgets that interact and
        engage with the current passage, optionally calling out to external
        APIs.
      </p>
      <p>
        We are also experimenting with Firebase for persistence. Offline
        use is also planned as is packaging DeepReader up as an app for
        mobile use.
      </p>
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex';

import Pagination from '@/components/Pagination';

export default {
  props: [
    'linker',
  ],
  computed: {
    ...mapState(['passage', 'interlinear']),
    ...mapGetters(['textClasses']),
  },
  mounted() {
    window.addEventListener('keyup', this.handleKeyUp);
  },
  beforeDestroy() {
    window.removeEventListener('keyup', this.handleKeyUp);
  },
  methods: {
    handleWordSelect(word) {
      this.$store.commit('setSelectedWord', word);
    },
    handleKeyUp(e) {
      if (e.key === 'ArrowLeft') {
        if (this.passage.prev) {
          this.$router.push(this.linker(this.passage.prev));
        }
      } else if (e.key === 'ArrowRight') {
        if (this.passage.next) {
          this.$router.push(this.linker(this.passage.next));
        }
      }
    },
  },
  components: {
    Pagination,
  },
  directives: {
    fragment(el, binding) {
      if (binding.value) {
        el.innerHTML = '';
        el.appendChild(binding.value);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
#text {
  clear: both;
  word-spacing: 0.3em;
  color: #333;
  .word {
    display: inline-block;
    margin-right: 0.5em;
    margin-bottom: 0.5em;
    cursor: pointer;
  }
  .verse-num {
    color: #999;
    font-family: $widget-font-family;
    font-size: 60%;
  }
  .gls {
    display: inline-block;
    font-size: 75%;
    color: gray;
  }
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
