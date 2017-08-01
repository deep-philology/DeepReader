<template>
  <div class="root">
    <header>
      <div class="reader-nav">
        <router-link to="cts">CTS API (Perseids)</router-link>
        &bull;
        <router-link to="cite-services">cite-services</router-link>
        &bull;
        <router-link to="morphgnt">MorphGNT API</router-link>
      </div>
      <h1>DeepReader (CTS)</h1>
    </header>
    <div class="grid-wrapper">
      <div class="left">
        <text-inventory v-if="textGroup"></text-inventory>
        <text-group v-if="work"></text-group>
        <work v-if="passage"></work>
      </div>

      <div class="main">
        <text-inventory v-if="!textGroup && !work && !passage"></text-inventory>
        <text-group v-if="textGroup && !work && !passage"></text-group>
        <work v-if="work && !passage"></work>
        <passage v-if="passage" :linker="passageLink"></passage>
      </div>

      <div class="right">
        <text-formatting v-if="passage"></text-formatting>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import * as URN from 'urn-lib';
import Passage from '@/components/Passage';
import TextFormatting from '@/widgets/TextFormatting';

import TextInventory from '@/cts/widgets/TextInventory';
import TextGroup from '@/cts/widgets/TextGroup';
import Work from '@/cts/widgets/Work';
import cts from '@/cts';


export default {
  name: 'reader',
  created() {
    this.$store.commit('setCTSReader', { passage: null });
    this.fetchData();
  },
  data() {
    return {
      query: null,
    };
  },
  computed: {
    ...mapState({
      textGroup: state => state.cts.textGroup,
      work: state => state.cts.work,
    }),
    ...mapState(['user', 'passage']),
  },
  watch: {
    $route: 'fetchData',
  },
  methods: {
    fetchData() {
      const urn = this.$route.query.urn;
      this.$store.commit('cts/setTextGroups', null);
      this.$store.commit('cts/setTextGroup', null);
      this.$store.commit('cts/setWorks', null);
      this.$store.commit('cts/setWork', null);
      this.$store.commit('setCTSReader', { passage: null });
      if (urn === undefined) {
        this.$store.dispatch('cts/loadTextGroups', 'urn:cts:greekLit');
      } else {
        const parsed = URN.RFC2141.parse(urn);
        const [segNS, segWork, segPassage] = parsed.nss.split(':');
        this.$store.dispatch('cts/loadTextGroups', `urn:cts:${segNS}`);
        if (segWork) {
          const [textGroupID, textGroupWorkID, editionID] = segWork.split('.');
          this.$store.dispatch('cts/loadTextGroup', `urn:cts:${segNS}:${textGroupID}`);
          if (textGroupWorkID) {
            this.$store.dispatch('cts/loadWork', `urn:cts:${segNS}:${textGroupID}.${textGroupWorkID}`);
          }
          if (!segPassage && editionID) {
            this.$store.dispatch('cts/loadEdition', `urn:cts:${segNS}:${textGroupID}.${textGroupWorkID}.${editionID}`).then((edition) => {
              this.$router.push({ query: { urn: edition.firstPassageURN } });
            });
          }
        }
        if (segPassage) {
          // passage urn
          cts.passage(`urn:cts:${segNS}:${segWork}:${segPassage}`).then((passage) => {
            this.query = this.$route.query; // @@@ do we need this?
            this.$store.commit('setCTSReader', { passage });
          });
        }
      }
    },
    passageLink(urn) {
      const { query } = this;
      if (urn) {
        return {
          query: Object.assign({}, query, { urn }),
        };
      }
      return null;
    },
  },
  components: {
    Passage,
    TextFormatting,
    TextInventory,
    TextGroup,
    Work,
  },
};
</script>

<style lang="scss">

  /* TEI */

  .TEI {
    .milestone {
      color: $text-milestone-color;
      font-family: $widget-font-family;
      font-size: 60%;
    }
    .said {
      .label {
        font-weight: bold;
      }
    }
    .l .n {
      color: $text-milestone-color;
      font-family: $widget-font-family;
      font-size: 60%;
    }
  }
</style>
