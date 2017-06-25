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
      <h1>DeepReader</h1>
    </header>
    <div class="grid-wrapper">
      <div class="left">
      </div>

      <div class="main">
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

      <div class="right">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'homepage',
  data() {
    return {
      query: null,
    };
  },
  mounted() {
    this.$log.log('Homepage mounted');
  },
};
</script>

<style lang="scss">
</style>
