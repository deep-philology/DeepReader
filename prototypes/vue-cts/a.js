const fetch = require('node-fetch');
const Bluebird = require('bluebird');

fetch.Promise = Bluebird;

fetch('http://www.perseus.tufts.edu/hopper/CTS?request=GetCapabilities')
  .then(res => {
    return res.text()
  })
  .then(blob => {
    parser = new DOMParser();
    xmlDoc = parser.parseFromString(blob, "text/xml");
    console.log(xmlDoc);
  });
