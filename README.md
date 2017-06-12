# DeepReader

DeepReader is a highly modular, Vue.js-based online reading environment designed for deep reading of texts with integrated learning tools.

It is particulary intended for the study of classical languages such as Ancient Greek but could be applied to any texts with rich annotations. What is here is an early prototype using the MorphGNT API and the CTS protocol but we plan to support other text services as well.

If you hover over the reader, you'll see various pluggable widgets on the left and right. Those on the left are used to choose what passage to read, and those on the right are used to present additional information about the passage and its individual words, and to control the appearance of the passage.

You can expand or collapse any widget by clicking on its title. You can use the arrow keys on your keyboard to pagination between passages in a work.

Each widget is a separate Vue.js component. We are working to make it as simple as possible to develop new widgets that interact and engage with the current passage, optionally calling out to external APIs.

We are also experimenting with Firebase for persistence. Offline use is also planned as is packaging DeepReader up as an app for mobile use.

* [A Reference Model for Capabilities of Online Readers](https://github.com/deep-reader/DeepReader/wiki/A-Reference-Model-for-Capabilities-of-Online-Readers)

## Setup

To run DeepReader in development mode:

    npm install
    npm run dev

Presently, there are two readers accesible at these paths:

* CTS: http://localhost:5066/#/cts
* MorphGNT: http://localhost:5066/#/morphgnt
