<template>
  <div class="home">
    <h1
      style="
        font-family: 'Fira Sans';
        letter-spacing: 0.25em;
        color: rgba(255, 255, 255, 0.7);
      "
    >
      Blog
    </h1>
    <ul class="hs full">
      <div
        v-for="(blog, index) in filteredArticles(this.blogs)"
        :key="blog.slug + '_' + index"
      >
        <ArticleBlock
          :slug="blog.slug"
          :id="blog.id"
          :title="blog.title"
          :updated="blog.updated_at"
          :published="blog.created_at"
          :description="blog.description"
          :imgSrc="blog.feature_image"
        />
      </div>
    </ul>

    <h1
      style="
        font-family: 'Fira Sans';
        letter-spacing: 0.25em;
        color: rgba(255, 255, 255, 0.7);
      "
    >
      Portfolio
    </h1>

    <ul class="hs full">
      <div
        v-for="(project, index) in filteredArticles(this.projects)"
        :key="project.slug + '_' + index"
      >
        <ArticleBlock
          :slug="project.slug"
          :id="project.id"
          :title="project.title"
          :updated="project.updated_at"
          :published="project.created_at"
          :description="project.description"
          :imgSrc="project.feature_image"
        />
      </div>
    </ul>

    <h1
      style="
        font-family: 'Fira Sans';
        letter-spacing: 0.25em;
        color: rgba(255, 255, 255, 0.7);
      "
    >
      Notes
    </h1>
    <ul class="hs full">
      <div
        v-for="(note, index) in filteredArticles(this.notes)"
        :key="note.slug + '_' + index"
      >
        <ArticleBlock
          :slug="note.slug"
          :id="note.id"
          :title="note.title"
          :updated="note.updated_at"
          :published="note.created_at"
          :description="note.description"
          :imgSrc="note.feature_image"
        />
      </div>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
import ArticleBlock from "@/components/ArticleBlock.vue";
// import Flickity from "vue-flickity";
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
export default {
  name: "Home",
  data() {
    return {
      blogs: [],
      notes: [],
      projects: [],

      flickityOptions: {
        initialIndex: 0,
        prevNextButtons: true,
        pageDots: true,
        wrapAround: true,
        // any options from Flickity can be used
      },
    };
  },
  //
  created() {
    let one = "http://localhost:5000/api/blogs";
    let two = "http://localhost:5000/api/notes";
    let three = "http://localhost:5000/api/projects";

    const requestOne = axios.get(one);
    const requestTwo = axios.get(two);
    const requestThree = axios.get(three);

    axios
      .all([requestOne, requestTwo, requestThree])
      .then(
        axios.spread((...responses) => {
          this.blogs = responses[0].data.all_blogs;
          this.notes = responses[1].data.all_notes;
          this.projects = responses[2].data.all_projects;
          // use/access the results
        })
      )
      .catch((errors) => {
        // react on errors.
        console.log(errors.response);
      });
    // axios
    //   .get("http://localhost:5000/api/blogs")
    //   .then((response) => {
    //     this.posts = response.data.all_blogs;
    //     // for (var i = 0; i < this.posts.length; i++) {
    //     //   this.posts[i].feature_image = require(this.posts[i].feature_image);
    //     // }
    //   })
    //   .catch((error) => {
    //     console.log(error.response);
    //   });
  },
  components: {
    ArticleBlock,
    // Flickity,
  },
  methods: {
    filteredArticles(arr) {
      let result = [];
      for (let i = 0; i < arr.length; i++) {
        if (JSON.parse(arr[i].published)) {
          result.push(arr[i]);
        }
      }
      return result;
    },
  },
};
</script>

<style>
.home {
  padding: var(--gutter) 0;
  display: grid;
  grid-gap: var(--gutter) 0;
  grid-template-columns: var(--gutter) 1fr var(--gutter);
  align-content: start;
  width: 60vw;
  border-radius: 8px;
}

.home > * {
  grid-column: 2 / -2;
}

.home > .full {
  grid-column: 1 / -1;
}

.hs {
  display: grid;
  grid-gap: 60px;
  grid-template-columns: 10px;
  /* grid-template-rows: minmax(150px, 1fr); */
  grid-auto-flow: column;
  grid-auto-columns: 300px;

  overflow-x: scroll;
  scroll-snap-type: x proximity;
  padding-bottom: calc(0.75 * var(--gutter));
  margin-bottom: calc(-0.25 * var(--gutter));
}

.hs:before,
.hs:after {
  content: "";
  width: 10px;
}

/* Demo styles */

html,
body {
  height: 100%;
}

body {
  display: grid;
  place-items: center;
  background: #070707;
}

ul {
  list-style: none;
  padding: 0;
}

h1 {
  margin-bottom: 0;
  margin-top: 8vh;
}

.home {
  background: #111111;
  overflow-y: scroll;
}

.hs > li,
.item {
  scroll-snap-align: center;
  padding: calc(var(--gutter) / 2 * 1.5);
  display: flexbox;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: rgb(6, 8, 9);
  border-radius: 8px;
  border: 3px solid rgba(180, 159, 187, 0.144) !important;
  height: 420px;
  width: 300px;
  text-decoration: none;
}

.a {
  text-decoration: none;
}

.item:hover {
  filter: saturate(150%) brightness(160%);
}

.no-scrollbar {
  scrollbar-width: none;
  margin-bottom: 0;
  padding-bottom: 0;
}
.no-scrollbar::-webkit-scrollbar {
  display: none;
}
:root {
  --gutter: 20px;
}
</style>


