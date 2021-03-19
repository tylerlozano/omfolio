const hljs = require('highlight.js');

const lang = process.argv[2];
const code = process.argv[3];
hljs.registerLanguage(lang, require('highlight.js/lib/languages/' + lang));

console.log(hljs.highlight(lang, code).value)