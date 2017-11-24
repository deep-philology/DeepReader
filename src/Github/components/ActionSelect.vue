<template>
  <widget>
    <span slot="header">Action Select</span>
    <div slot="body">
      <ul>
        <li v-for="action in actions">
          <router-link class="click" :to="action">
            {{action}}
          </router-link>
        </li>
      </ul>
    </div>
  </widget>
</template>

<script>
  import Widget from '@/components/Widget';

  export default {
    props: [
      'actions',
    ],
    components: {
      Widget,
    },
  };
</script>
