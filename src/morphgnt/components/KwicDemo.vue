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
      <h1>DeepReader (MorphGNT KWIC Demo)</h1>
    </header>
    <div class="grid-wrapper">
      <div class="left">
      </div>

      <div class="main">
        <kwic2></kwic2>
      </div>

      <div class="right">
      </div>
    </div>
  </div>
</template>

<script>
  import Kwic2 from '@/morphgnt/widgets/Kwic2';

  export default {
    components: {
      Kwic2,
    },
  };
</script>
