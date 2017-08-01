<template>
  <div id="passage">
    <pagination
      :prev="linker(passage.prev)"
      :next="linker(passage.next)"
      :title="passage.title">
    </pagination>
    <div id="text" :class="textClasses" v-fragment="passage.fragment">
      <p>
        <div v-for="word in passage.words" class="word unit">
          <span class="verse-num" v-if="word.id.slice(8, 11) == '001'">{{ parseInt(word.id.slice(5, 8)) }}</span><!--
          --><span :key="word.id" :id="word.id" :class="['txt', ...word.classes]" @click="handleWordSelect(word)">{{ word.text }}</span><br>
          <template v-if="interlinear">
            <span class="gls">
              <span class="pos">{{ word.pos }}</span><!--
              --><span v-if="word.mood">.{{ word.tense }}{{ word.voice }}{{ word.mood }}</span><!--
              --><span v-if="word.number">.{{ word.person }}{{ word.case }}{{ word.number }}{{ word.gender }}</span><!--
              --><br>{{ word.lemma }}<br>
            </span>
          </template>
        </div>
      </p>
    </div>
    <pagination
      :prev="linker(passage.prev)"
      :next="linker(passage.next)"
      :title="passage.title">
    </pagination>
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
      const fragment = binding.value;
      if (fragment && fragment.childElementCount > 0) {
        el.innerHTML = '';
        el.appendChild(fragment);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
  #passage {
    margin: 20px 50px;
  }
  #text {
    clear: both;
    color: $main-text-color;

    .word {
      cursor: pointer;
      .verse-num {
        color: $text-milestone-color;
        font-family: $widget-font-family;
        font-size: 60%;
        margin-right: 0.5em;
      }
    }
    .unit {
      display: inline-block;
      margin-bottom: 0.5em;
      margin-right: 0.5em;
      user-select: text;
    }
    .txt {
      display: inline-block;
    }
    .gls {
      display: inline-block;
      font-size: 75%;
      color: $interlinear-color;
    }
  }
</style>
