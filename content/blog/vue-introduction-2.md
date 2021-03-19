---
title: Create a Single Page App with Vue CLI
description: 
Single Page Apps (SPA) work in the browser and don't require page reloads or updates since content is downloaded automatically. Since SPAs are so responsive, they provide a seamless and linear user experience perfect for building dynamic platforms and mobile apps.
feature_image: omfolio.svg
published: true
link: false
tags: Vue, SPA, Web, Tutorial
---

The **Vue command line interface (CLI)** speeds up the development process by creating the foundation of a Vue app based on a selection of features both native and external to Vue, e.g. whether you want to use **Vue router** or configure assets with **webpack**. Once initialized you can take advantage of Vue's **Hot Module Replacement (HMR)** to modify your app during runtime for immediate feedback. This article is part one of a series on Vue using interactive examples to illustrate Vue's key features.

### Prerequisites

1. An IDE. [Visual Studio Code](https://code.visualstudio.com/download) comes highly recommended.
2. Install [npm](https://nodejs.org/en/download/), a package manager for node.
3. Install or Update Vue CLI to version 4.5.11 (check with `vue -V`):  
    `npm install -g @vue/cli`

### Getting Started

If you want to look ahead at the finished example for this article, it can be found [here](https://github.com/tylerlozano/example-spa).

Open your terminal in the directory you wish to host the project. Initialize project with `vue create example-spa`. It will give you a list of presets to choose from, arrow down to *Manually select features* (you can also save your selected options as a preset for future projects.)
  
You'll be given a list of options to choose from. Choose the following: 
  
      ❯ Router  
      ❯ Vuex  
  
Then select the following as they appear:
  
      ❯ Vue version 3.x  
      ❯ History mode for router  

*History mode uses `history.pushState` API to achieve URL navigation without a page reload* [^1]

      ❯ ESLint + Prettier  
      ❯ Lint on save  
      ❯ Dedicated config files  

[^1]: [History Mode](https://router.vuejs.org/guide/essentials/history-mode.html) 
  
### App Structure
Our directory should now look like (view with [`tree -L 3`](https://rschu.me/list-a-directory-with-tree-command-on-mac-os-x-3b2d4c4a4827)):

<img alt="folders" src="/media/vue-folders.png" style="margin-left: max-width: 75vw;"></img>  

> * **public/index.html &mdash;** Entry point of your application where built files will be auto-injected
> * **src/main.js &mdash;** Initializes the root component into a element in your index.html
> * **src/App.vue &mdash;** Root component of your application and where you define global app behaviour
> * **public &mdash;** Static resources placed in here will be copied without passing through webpack
> * **src/assets &mdash;** Where you put any assets that are imported into your components
> * **src/components &mdash;** All the components of the projects that are not routed to as pages
> * **src/router &mdash;** All the routes of your projects, usually stored in an index.js file
> * **src/store &mdash;** Folder to store the Vuex constants and modify Vuex through index.js
> * **src/views &mdash;** Components that represents a whole page and has an associated route go here

There's also a number of config files for *Webpack, Node, Eslint, Git, and Babel* -- don't worry about these while you're starting out.

### Routes

Go to your command line and make sure you're in *example-spa* directory, then `npm run serve`. After some initial building, it should launch on [localhost:8080](http://localhost:8080). Let's take a top-down view to understand the structure of the app.  

`App.vue`: 
``` javascript
<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </div>
  <router-view />
</template>
```

As you can probably tell, *App.vue* is our root component, so any view component has it as an ancestor, hence anything in *App.vue* that's not `<router-view />` is persisted across every page. Looking at `<router-link to="/">Home</router-link> ` we notice that the default page `/` will load our *Home view*. But how does it know this? That's defined in the `index.js` of our `router` directory.

``` javascript
const routes = [
    /* Here the path '/' is mapped to our Home view */
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  }
];
```

The above `routes` array links **url paths** to **view components** in the *views* directory. You can also nest *views* just like regular components, this is called **nested routes** (important if you want to create a *login view* for routes only available upon login, or a *Navbar view* so some views can be fullscreen. [^3]) Notice that the `About` and `Home` objects look different, that's because `About` is being separated through Webpack's **code splitting** into a javascript chunk to be **lazy loaded** when the route is visited. By loading the app piece-wise, we offset putting everything upfront and slowing down the SPA when it is first visited.[^4] The comment within the `import` statement is called a **magic comment** by Webpack and is used to give the javascript chunk a name instead of some nondescript number.[^5] 

[^3]: [Nested Routes](https://router.vuejs.org/guide/essentials/nested-routes.html)
[^4]: [Lazy Loading](https://router.vuejs.org/guide/advanced/lazy-loading.html)
[^5]: [Magic Comments](https://webpack.js.org/api/module-methods/#magic-comments)

<img alt="lazy loading" src="/media/lazy-load.png" style="width: 60vw;"></img>

You can verify this behavior by inspecting the homepage of your app with dev tools, going to the network section and filtering for javascript. Refresh the page and notice *App.js* loads, then visit the *About* route and you'll notice a chunk called *about.js* added to the list. Cool, right? :-)


### Component Composition

Take a peek into *Home.vue*:  
  
``` javascript
<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  components: {
    HelloWorld
  }
};
</script>
```

 In the template of *Hello.vue* we see it will load an image followed by the `HelloWorld` component which is passed a **prop** `msg` with a string value. A **prop** is the way a parent component communicates with child components, and it can also go the other way with children emitting **events** to be handled by ancestors. If we change the value of `msg` to `Hello World!` and save, we should see it displayed immediately on our app's home page thanks to **HMR.**

 > One important thing to note is that separation of concerns is not equal to separation of file types. In modern UI development, we have found that instead of dividing the codebase into three huge layers that interweave with one another, it makes much more sense to divide them into loosely-coupled components and compose them. [^2]

 [^2]: [Component Composition](https://vuejs.org/v2/guide/single-file-components.html)

A Vue component is typically organized into 3 blocks: template for structure, script for app logic, and style for aesthetics. To give a taste of the interplay between the 3 blocks, lets change it up a bit. In the `<script>` of your `Home` component let's add the following under `export default`:

``` javascript
data() {
    return {
    messages: ["Hello", "World!"],
    fontSize: 6,
    };
},
```

We can reference data from our script with the `this` keyword. Go ahead and replace the `HelloWorld` component in the template with the following:

``` javascript
<div v-for="(msg, idx) in this.messages" :key="idx">
      <p :id="'c' + idx" :style="{ 'font-size': fontSize + 'rem' }">
        {{ msg }}
      </p>
    </div>
```

This **Vue directive** `v-for` iterates over the data to the right of `in`, `this.messages`. We can display text data within html tags with **mustache braces** `{{ }}`. Further, we can identify these `<p>` tags separately in our `<style>` block by adding their unique *index* to their `#id`. We can also do inline styling with style binding using `:style`.

``` css
<style>
#c0 {
  color: red;
}
#c1 {
  color: blue;
}
</style>
```

Now if you save there should be an error that *The "HelloWorld" component has been registered but not used*. That's fine, just comment out or delete any line with `HelloWorld` -- if you import a component or have it under `components` in your script, then you have to use it or you get this error (if you're using VSC you can quickly comment out an entire line with **[cmd] + [/]**).  

### Communication

We already know how to pass information to child components in our template through **props**, but what about from child to parent? This is where **events** come into play. Define a new component in your *components* directory called *MyButton.vue*:

``` javascript
<template>
  <button
    :style="{ background: background, color: color }"
    @click="$emit('my-event')"
  >
    My Button
  </button>
</template>

<script>
export default {
  props: {
    color: {
      type: String,
      required: true,
    },
    background: {
      type: String,
      required: false,
    },
  },
};
</script>
```

This is a simple button component that takes two **props** to style the button, `background` and `color`, 
and **emits** a **custom event** called `my-event` on click (all events are automatically lowercased, so *do not use camelCase*.)[^6]  The `@` is syntactic sugar for a Vue directive `v-on:` which is used to listen to [DOM events](https://www.w3schools.com/jsref/dom_obj_event.asp) and run some JavaScript when they’re triggered. 
[^6]: [Custom Events](https://vuejs.org/v2/guide/components-custom-events.html)

Let's snazz up the *About view* with our new *MyButton* component.

``` javascript
<template>
  <div>
    <MyButton @my-event="toggleValue()" color="black" background="orange" />
    <span class="base" :class="useTheme && 'active'">
      {{ this.useTheme }}
    </span>
  </div>
</template>

<script>
import MyButton from "@/components/MyButton.vue";
export default {
  data() {
    return {
      useTheme: false,
    };
  },
  methods: {
    toggleValue() {
      this.useTheme = !this.useTheme;
    },
  },
  components: {
    MyButton,
  },
};
</script>

<style>
.base {
  font-size: 5rem;
  color: black;
}
.active {
  color: purple;
  font-weight: bold;
}
</style>
```

The *event* we want to communicate to the parent must be registered on the child component that emits that *event*.
Just as with *click*, we use `@my-event` followed by some javascript we want to run, in this case a custom *method* `toggleValue()` defined in `methods`. The `toggleValue()` method inverts the boolean value of `useTheme` which defaults to `false` as defined in `data()`. The `span` element containing our text is using a base class style called `base` and a **conditional class** `active` which is activated using what's called a **guard expression**. Simply put, if `useTheme` is `false` the `&&` expression will short-circuit and no theme is applied, if it's `true` then the expression evaluates to `active`. [^7] 
[^7]: [Conditional Class Bindings](https://michaelnthiessen.com/conditional-class-binding-vue/)

<img alt="communication" src="/media/communication.png" style="opacity: 70%; width: 70%; margin-left: auto; margin-right: auto; align-content: center; display: block;"></img>

Only a *parent* of the *child* component can *listen* for *events* that child emits, and likewise only a *parent* can pass *props* to its *child*. In order to get around this limitation and interact with distant components a number of viable strategies exist, in ascending order of recommendation[^8]: 
[^8]: [Event Strategies](https://stackoverflow.com/questions/63471824/vue-js-3-event-bus)
> * Re-emit the event
> * **Event bus**
> * **Publish-subscriber** programming pattern
> * **Vue 3 Composition API**
> * **Vuex** the state management pattern + library for Vue

The **Vue 3 Composition API** is highly recommended for smaller projects, but at the time of this writing it is still without **Vuex**'s debugging capabilities and rich plugin ecosystem. The other 3 are mostly historical approaches to the problem, and while they may still have use cases, the latter 2 should be sufficient 99% of the time.

Back to our app, after defining and saving *MyButton.vue* and *About.vue* navigate to the *about page* if you haven't already and click *My Button* a few times to see our active styling apply and un-apply to the text. Let the text display `true` and navigate to the *home page* and back. You'll notice our change is no longer there. That's because data is lost when we navigated away from the page. The same applies if you refresh the page. To get around this loss of state we also use **Vuex** or the **Vue 3 Composition API** to persist *state* across the entire application.

The next post in this series will cover **component lifecycle**, **Vuex**, and the new **Composition API** which will continue where we left off.

<div class="next" style="font-family: 'Fira Sans'; color: rgba(241, 245, 245, 0.911); text-align: center; font-weight: 400; margin-top: 8vh;"> Next &nbsp; &#8594; &nbsp; <em>In Development</em> </div>

---

### Resources

* [Vue Docs](https://vuejs.org/v2/guide/)
* [Vue Community](https://vuejs.org/v2/guide/join.html) &mdash; *many thanks to the Vue discord especially*
* [Program With Erik](https://www.youtube.com/channel/UCshZ3rdoCLjDYuTR_RBubzw) &mdash; *excellent Vue Youtube channel*
* [Vue Mastery](https://www.vuemastery.com/courses/) &mdash; *free lessons at the start, well worth the money to continue*

---
















