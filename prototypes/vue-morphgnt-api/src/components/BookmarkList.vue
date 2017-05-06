<template>
  <widget>
    <span slot="header">Bookmarks</span>
    <div slot="body">
      <button v-if="passage" @click="saveBookmark">save</button>
      <div v-for="bookmark in bookmarks" class="bookmark">
        <span class="remove" @click="removeBookmark(bookmark)">remove</span>
        <router-link :to="$parent.passageLink($parent.query, bookmark.resource)">{{ bookmark.title }}</router-link>
      </div>
    </div>
  </widget>
</template>

<script>
  import { mapGetters } from 'vuex';
  import Widget from '@/components/Widget';
  import app from '@/firebase';

  const db = app.database();
  const bookmarksRef = db.ref('bookmarks');

  export default {
    created() {
      this.$store.dispatch('setBookmarksRef', this.userBookmarks());
    },
    computed: {
      passage() {
        return this.$parent.passage;
      },
      ...mapGetters(['user', 'bookmarks']),
    },
    methods: {
      userBookmarks() {
        return bookmarksRef.child(this.user.uid);
      },
      saveBookmark() {
        this.userBookmarks().push({
          resource: this.passage['@id'],
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
  a {
    display: block;
    color: inherit;
    text-decoration: none;
    padding: 2px 5px;
    &:hover {
      color: #666;
    }
  }
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
