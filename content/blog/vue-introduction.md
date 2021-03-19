---
title: State Management in Vue - When, Where, & How
description: 
Vue has a range of solutions for state management from the native Composition API in Vue 3 to the Redux-like library 
and pattern Vuex. Both solve similar solutions with various pros and cons. We approach both solving a similar problem to
better compare and contrast when to use which where.
feature_image: omfolio.svg
published: true
link: false
tags: Vue, SPA, Web, Tutorial
---

### State Management

Let's take a look at the default **Vuex store** that **VUE CLI** created for us at the start in *store/index.js*:

``` javascript
import { createStore } from "vuex";

export default createStore({
  state: {},
  mutations: {},
  actions: {},
  modules: {}
});
```
...