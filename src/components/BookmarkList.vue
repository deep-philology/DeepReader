<template>
  <widget>
    <span slot="header">Bookmarks</span>
    <div slot="body">
      <button v-if="passage" @click="saveBookmark">save</button>
      <div v-for="bookmark in bookmarks" class="bookmark">
        <span class="remove" @click="removeBookmark(bookmark)">remove</span>
        <router-link :to="$parent.passageLink(bookmark.resource)">{{ bookmark.title }}</router-link>
      </div>
    </div>
  </widget>
</template>

<script>
  import { mapState } from 'vuex';
  import Widget from '@/components/Widget';
  import app from '@/firebase';

  const db = app.database();
  const bookmarksRef = db.ref('bookmarks');

  export default {
    created() {
      this.$store.dispatch('setBookmarksRef', this.userBookmarks());
    },
    computed: {
      ...mapState(['user', 'passage', 'bookmarks']),
    },
    methods: {
      userBookmarks() {
        return bookmarksRef.child(this.user.uid);
      },
      saveBookmark() {
        this.userBookmarks().push({
          resource: this.passage.id,
          title: this.passage.title,
        });
      },
      removeBookmark(bookmark) {
        this.userBookmarks().child(bookmark['.key']).set(null);
      },
    },
    components: {
      Widget,
    },
  };
</script>

<style lang="scss" scoped>
  button {
    margin-bottom: 0.5em;
  }
  .bookmark {
    padding: 2px 0;
    .remove {
      color: transparent;
      float: right;
      cursor: pointer;
    }
    &:hover {
      .remove {
        transition: color 0.2s ease-in-out;
        color: inherit;
        &:hover {
          color: #C00;
        }
      }
    }
  }
</style>
