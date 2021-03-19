const katex = require('katex');
var str = process.argv[2];
var display = process.argv[3] === "true";

console.log(katex.renderToString(str, { displayMode: display, }))
