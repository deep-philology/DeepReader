<template>
  <widget>
    <span slot="header">Issue Select</span>
    <div slot="body">
      <ul>
        <li v-for="issue in issues">
            #{{ issue.number }}: {{ issue.title }}
        </li>
      </ul>
    </div>
  </widget>
</template>

<script>
  import { mapState } from 'vuex';
  import Widget from '@/components/Widget';

  export default {
    props: [
      'issues',
    ],
    computed: {
      ...mapState(['user']),
    },
    components: {
      Widget,
    },
  };
</script>
