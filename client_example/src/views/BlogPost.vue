<template>
  <div class="blog-post">
    <h1
      style="
        font-family: 'Fira Sans';
        font-size: 3rem;
        color: whitesmoke;
        margin-top: 0vh !important;
        padding-top: 2vh !important;
      "
    >
      {{ post.title }}
    </h1>
    <p
      style="
        text-align: left;
        margin-left: 5vw;
        margin-right: 5vw;
        padding-bottom: 2vh;
      "
    >
      {{ post.description }}
    </p>
    <div class="content" v-html="post.content"></div>
  </div>
</template>


<script>
import "../../node_modules/katex/dist/katex.css";
import axios from "axios";
// import vueStickySidebar from "vue-sticky-sidebar";
export default {
  name: "blog-post",
  data() {
    return {
      post: {},
    };
  },
  //
  created() {
    axios
      .get("http://127.0.0.1:5000/api/article/" + this.$route.params.id)
      .then((response) => {
        this.post = response.data;
        console.log(this.id);
      });
  },

  components: {
    // "vue-sticky-sidebar": vueStickySidebar,
  },
  // data() {
  //   return {
  //     post: "# My Markdown \n Strings are cool!",
  //     html: "blah",
  //   };
  // },

  props: {
    id_: String,
  },
  computed: {
    cssVars() {
      return {
        "--bg": ' url("this.post.feature_image")',
      };
    },
  },
};
</script>

  <!-- container
  image 100% wide
  image overlay
  title 
  info-bar: picture-badge name date-of-writing date-last-updated

  container
  html with code, math, etc

  side scroll based on headers

  keywords -> topic -> notes

  github issues comments-->

<style>
/* div.blog-post > header-image {
  height: 100vh;
  width: 100vw;
} */

#footnotes {
  margin: 0px 0px 16px !important;
}
ol.footnotes-list {
  /* transform: translateX(-2em);
  margin-top: 2em;
  margin-left: 0; */
  margin-top: 3em !important;
  line-height: 1 !important;
  font-size: calc(1px + 1.2vw) !important;
}

.footnote-backref {
  color: rgb(53, 226, 183) !important;
  font-size: calc(14px + 0.25vw);
  font-weight: bold;
  margin-left: 0.5rem;
}

[id*="fnref"] {
  margin-left: 0.3rem;
  font-family: "Iceland" !important;
  color: rgb(53, 226, 183) !important;
}
[id*="fnref"]:hover {
  color: rgba(53, 226, 183, 0.438) !important;
}

a.footnote-backref:hover {
  color: rgba(53, 226, 183, 0.438) !important;
}

hr.footnotes-sep {
  margin-top: 8vh !important;
  border-top: 0px !important;
  border: none;
}

hr.footnotes-sep::before {
  content: "\203B  References";
  font-family: "Fira Sans";
  font-weight: 300;
  display: flex;
  font-size: calc(28px + 0.25vw) !important;
  padding: 0;
  color: rgb(245, 245, 245);
  margin-right: 0.25em;
  opacity: 0.8 !important;
}

div.blog-post {
  width: 100%;
  background: rgb(12, 30, 39);
  /* width: 100vw;
  height: 100vh; */
  line-height: 2;
  display: flexbox;
  position: absolute;
  top: 0;
  left: 0;
}

div.below-hero {
  position: relative;
  background: rgba(8, 20, 26, 1);
  width: 100vw;
}

div.hero {
  opacity: 0.9;
  width: 100vw;
  height: 100vh;

  background-image: linear-gradient(rgba(12, 30, 39, 0) 15vh, rgb(12, 30, 39)),
    var(--bg);
  /* url("../content/blog/0/media/website2.jpg"); */
  background-size: cover;
  /* background-position: center center;
  background-repeat: no-repeat; */
  margin-bottom: 5vh;
}

div.hero-content {
  margin-bottom: 5vh;
  display: flexbox !important;
  float: left;
}
div.hero-content > h1 {
  color: rgba(221, 220, 220, 0.931);
  position: relative;
  padding-top: 70vh;
  margin-left: 11vw;
  text-align: left;
  font-family: "Fira Sans", sans-serif;
  font-weight: 200;
  font-size: calc(40px + 0.8vw) !important;
}

div.hero-content > p {
  color: rgba(221, 220, 220, 0.829);
  margin-left: calc(5px + 11vw);
  margin-right: 25vw;
  text-align: left;
  font-family: "Fira Sans", sans-serif;
  font-size: calc(20px + 0.25vw) !important;
  font-weight: 300;
  margin-bottom: 3rem;
}

div.list-group.infobar.list-group-horizontal {
  margin-top: 1vh;
  margin-left: 0vw !important;
  margin-bottom: 2vh !important;
}
/* div.info {
  margin-left: 8vw;
  margin-bottom: 3vw;
} */
/* 
h1.card-title {
  opacity: 1 !important;
  position: absolute;
  bottom: 0;
  left: 5;
  padding-bottom: 3.5rem;
  font-family: "Fira Sans", sans-serif;
  font-size: 4rem;
}
p.card-text {
  opacity: 1 !important;
  position: absolute;
  bottom: 0;
  left: 5;
  padding-top: 1rem;
  padding-bottom: 0rem;
  font-family: "Monserrat", sans-serif;
  font-size: 1.5rem;
}
p.sm-1 {
  opacity: 1 !important;
  font-family: "Monserrat", sans-serif;
  font-size: 1rem;
  font-weight: 500;
  color: rgb(255, 255, 255) !important;
} */

.list-group-item {
  padding: 0;
  background-color: rgba(0, 0, 0, 0);
  border: 0px;
  line-height: 1.5vh;
}

/* content  */
div.content {
  width: 62vw;
  float: left;
  margin-left: 10vw;
  position: relative;
  font-family: "Fira Sans" !important;
  line-height: 2;

  font-size: calc(16px + 0.25vw);
  font-weight: 300;
  color: rgba(250, 252, 252, 0.952) !important;
  background: transparent;
  /*background: rgb(19, 19, 19);*/
  text-align: left;
  /* margin-left: 15vw; */
  margin-bottom: 3vh;
}

p {
  font-family: "Fira Sans";
  font-size: calc(16px + 0.25vw);
  font-weight: 300;
  color: rgba(250, 252, 252, 0.952);
  background: transparent;
  /*background: rgb(19, 19, 19);*/
  /* margin-left: 15vw; */
}
em {
  color: rgba(247, 244, 178, 0.795) !important;
}
a {
  color: rgba(62, 129, 192, 0.863);
}

a:hover {
  color: rgba(132, 185, 235, 0.986);
  text-decoration: none;
}

div.content > hr {
  border-top: 0px dashed rgba(217, 243, 230, 0.356);
  margin-top: 2vh;
  margin-bottom: 2vh;
}

img {
  margin-top: 3vh;
  margin-bottom: 3vh;
}
div.content >>> img,
div.content /deep/ img {
  display: block;
  height: auto;
  width: auto;
  /* even more control with max-width */
  max-width: 60vw;
  margin-left: auto;
  margin-right: auto;
  margin-top: 5vh;
  margin-bottom: 5vh;
  opacity: 0.8;
  align-content: center;
}

/* definition terms */
dd,
dt {
  font-family: "Rokkitt";
  margin-left: 0;
  text-align: left;
  font-size: calc(18px + 0.25vw);
  color: rgba(241, 245, 245, 0.993);
}

dl > dd > p {
  font-family: "Rokkitt";
  margin-top: 0 !important;
  margin-bottom: 0 !important;
  margin-left: 0;
  text-align: left;
  font-size: calc(18px + 0.25vw);
  color: rgba(241, 245, 245, 0.993);
}

dd {
  font-weight: 300;
}

dt {
  font-weight: 500;
}

/* math  */
div.content >>> katex {
  color: white;
  font-size: calc(16px + 0.25vw);
}

.katex .base {
  color: white;
}

.katex-display {
  font-size: calc(16px + 0.25vw);
}

/* eqno */
.mord {
  color: rgba(255, 255, 255, 0.836);
  font-size: calc(16px + 0.25vw);
}
ul,
ol,
li {
  text-align: left;
  color: rgba(233, 240, 240, 0.911);
  font-size: calc(16px + 0.25vw);
  font-weight: 400 !important;
  font-family: "Fira Sans";
  line-height: 1.6;
}

/* headings */
div.content > h1,
div.content > h2,
div.content > h3,
div.content > h4,
div.content > h5,
div.content > h6 {
  color: rgba(245, 245, 245, 0.863);
  font-family: "Exo", sans-serif;
  font-weight: 300;
  text-align: left;
  margin-top: 5vh;
  margin-bottom: 2vh;
}

div.content > h1 {
  font-size: calc(32px + 0.25vw);
}
div.content > h2 {
  font-size: calc(30px + 0.25vw);
}
div.content > h3 {
  font-size: calc(28px + 0.25vw);
}

div.content > h4 {
  font-size: calc(26px + 0.25vw);
}

div.content > h5 {
  font-size: calc(24px + 0.25vw);
}

/* block quote : source quotes questions etc*/
blockquote {
  background: #00293bce;
  /* border-left: 5px solid rgb(69, 138, 150); */
  margin: 1.5em 10px;
  padding: 0.5em 10px;
  quotes: "\201C""\201D""\2018""\2019";
  /* margin-left: 15vw; */
  width: auto;
  border-radius: 16px;
  max-height: 200vh;
  text-align: left;
  box-shadow: 0em 0em 0.8em 0em rgba(1, 8, 20, 0.658);
  margin-top: 3vh;
  margin-bottom: 3vh;

  /* */
  font-family: "Fira Sans" !important;
  font-weight: 400 !important;
  font-size: calc(16px + 0.25vw);
  text-align: left;
}

blockquote p {
  /* font-family: "Oxygen"; */
  font-family: "Fira Sans" !important;
  font-weight: 400 !important;
  font-size: calc(16px + 0.25vw);
  display: inline;
  text-align: left;
  color: rgba(199, 199, 199, 0.877);
}

/* blockquote:before {
  color: rgba(12, 223, 223, 0.801);
  content: open-quote;
  font-size: 4em;
  line-height: 0.1em;
  margin-right: 0.25em;
  vertical-align: -0.4em;
} */
/* blockquote:after {
  color: rgba(12, 223, 223, 0.801);
  content: close-quote;
  font-size: 4em;
  line-height: 0.1em;
  margin-right: 0.25em;
  vertical-align: -0.4em;
} */

/* .katex .base {
  margin-left: 1vw;
  margin-right: 1vw;

  font-weight: bold;
} */

/* block */
/* .katex-display {
  background: transparent;
  width: 60vw;
} */

/* code highlighting */

pre code,
code {
  font-family: "Source Code Pro" !important;

  font-size: calc(16px + 0.25vw);
  line-height: 1.3em;
  font-weight: 500;
}

pre {
  overflow-x: auto;
  width: auto;
  /* margin-left: 15vw; */
  text-align: left;
  white-space: pre-wrap;
  text-shadow: 0 0px 0px rgba(0, 0, 0, 0);
  background: #0250504d;
  color: #dcdcdcd5;
  padding: 0.5em;
  overflow: auto;
  border-radius: 8px;
  max-height: 65vh;
  box-shadow: 0em 0em 0.8em 0em rgba(0, 5, 3, 0.945);

  /* */
  font-family: "Source Code Pro", monospace !important;

  font-size: calc(16px + 0.25vw);
  line-height: 1.3em;
  font-weight: 500;

  margin-top: 3vh;
  margin-bottom: 3vh;
}

pre .language-python::before {
  content: "Python";
  display: block;
  font-size: calc(10px + 0.25vw);
  opacity: 0.5;
}

pre .language-css::before {
  content: "CSS";
  display: block;
  font-size: calc(10px + 0.25vw);
  opacity: 0.5;
}

pre .language-bash::before {
  content: "Bash";
  display: block;
  font-size: calc(10px + 0.25vw);
  opacity: 0.5;
}

/* TODO: CHANGE CONTENT */
pre .language-javascript::before {
  content: "Vue";
  display: block;
  font-size: calc(10px + 0.25vw);
  opacity: 0.5;
}

pre .language-c::before {
  content: "C";
  display: block;
  font-size: calc(10px + 0.25vw);
  opacity: 0.5;
}

code {
  color: #90f3a6c5;
  word-wrap: break-word;
}

/* don't touch below */

.hljs-keyword,
.hljs-literal,
.hljs-symbol,
.hljs-name {
  color: #569cd6e2;
}
.hljs-link {
  color: #569cd6e9;
  text-decoration: underline;
}

.hljs-built_in,
.hljs-type {
  color: #4ec9b0d9;
}

.hljs-number,
.hljs-class {
  color: #97e463de;
}

.hljs-string,
.hljs-meta-string {
  color: #b31ec7e1;
}

.hljs-regexp,
.hljs-template-tag {
  color: #ee6577ea;
}

.hljs-subst,
.hljs-function,
.hljs-title,
.hljs-params,
.hljs-formula {
  color: #dcdcdcee;
}

.hljs-comment,
.hljs-quote {
  color: #72db62da;
  font-style: italic;
}

.hljs-doctag {
  color: #608b4ed5;
}

.hljs-meta,
.hljs-meta-keyword,
.hljs-tag {
  color: #9b9b9b;
}

.hljs-variable,
.hljs-template-variable {
  color: #9347c5e1;
}

.hljs-attr,
.hljs-attribute,
.hljs-builtin-name {
  color: #b6bd5bd9;
}

.hljs-section {
  color: gold;
}

.hljs-emphasis {
  font-style: italic;
}

.hljs-strong {
  font-weight: bold;
}

.hljs-bullet,
.hljs-selector-tag,
.hljs-selector-id,
.hljs-selector-class,
.hljs-selector-attr,
.hljs-selector-pseudo {
  color: #d77dd7;
}

.hljs-addition {
  background-color: #206e1d;
  display: inline-block;
  width: 100%;
}

.hljs-deletion {
  background-color: #600;
  display: inline-block;
  width: 100%;
}
</style>
