<template>
  <router-link
    :to="{ name: 'BlogPost', params: { slug: slug, id: id } }"
    class="blog-link"
  >
    <li class="item" style="border: 1px solid rgba(100, 100, 100, 0.8)">
      <img
        :src="imgSrc"
        style="
          width: 100%;
          max-height: 40%;
          object-fit: contain;
          margin-top: 20px !important;
          margin-bottom: 2px !important;
        "
      />
      <p
        style="
          text-align: center !important;
          font-family: 'Fira Sans';
          font-weight: 300 !important;
          font-size: calc(10px + 0.25vw);
          color: rgba(155, 195, 255, 0.8) !important;
          margin-top: none !important;
        "
      >
        Written {{ published }} and Last Updated {{ updated }}
      </p>
      <h3
        style="
          margin-bottom: 0;
          font-family: 'Fira Sans';
          font-size: calc(16px + 0.25vw);
          color: rgba(200, 200, 200, 0.8);
        "
      >
        {{ title }}
      </h3>
      <p
        style="
          text-align: left;
          font-family: 'Fira Sans';
          font-size: calc(12px + 0.25vw);
          color: rgba(170, 200, 200, 0.8);
        "
      >
        {{ description.substring(0, 125) }}...
      </p>
    </li>
  </router-link>
</template>

<script>
import "../../node_modules/katex/dist/katex.css";
export default {
  data() {
    return {};
  },
  props: {
    id: {
      type: String,
      required: true,
    },
    slug: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
    imgSrc: {
      type: String,
      required: true,
    },

    updated: {
      type: String, // change to Date
      required: false,
    },

    published: {
      type: String, // change to Date
      required: false,
    },
  },
};
</script>


<style>
a {
  text-decoration: none;
}
</style>
            
    