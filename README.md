Project Euler
====================================================================


Currently, most of these solutions are written in Python because... well... high-precision math. But as it turns out, Project Euler problems are still insanely fun to solve in JavaScript as well -- especially utilizing some of the latest features from ECMAScript 2015 and up.

As such, I've made an index.html file will use System.js to import a solution file, compile it with Babel, and execute an exported solution runner function in the console. Applicable scripts currently start at solution #30.

To build and be able to run/serve files locally:

```
npm install jspm

jspm install
```
