import fetch from 'universal-fetch';
import xpath from 'xpath';
import teiXSL from '@/cts/tei.xsl';
import { sortBy } from '@/utils';

export default {
  url: 'http://cts.perseids.org/api/cts/',

  async textGroups(urn) {
    const url = `${this.url}?request=GetCapabilities&urn=${urn}`;
    const response = await fetch(url);
    const text = await response.text();
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(text, 'text/xml');
    const select = xpath.useNamespaces({ cts: 'http://chs.harvard.edu/xmlns/cts' });
    // console.log(select('//cts:TextInventory/cts:textgroup', xmlDoc)[0]);
    const textGroups = [];
    select('//cts:TextInventory/cts:textgroup', xmlDoc).forEach((textGroup) => {
      const textGroupURN = select('@urn', textGroup)[0].textContent;
      const groupName = select('cts:groupname', textGroup)[0].textContent;
      textGroups.push({ urn: textGroupURN, groupName });
    });
    textGroups.sort(sortBy('groupName', true, x => x.toUpperCase()));
    return textGroups;
  },

  async textGroup(urn) {
    const url = `${this.url}?request=GetCapabilities&urn=${urn}`;
    const response = await fetch(url);
    const text = await response.text();
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(text, 'text/xml');
    const select = xpath.useNamespaces({ cts: 'http://chs.harvard.edu/xmlns/cts' });
    const works = [];
    select('//cts:TextInventory/cts:textgroup/cts:work', xmlDoc).forEach((work) => {
      const workURN = select('@urn', work)[0].textContent;
      const title = select('cts:title', work)[0].textContent;
      works.push({ urn: workURN, title });
    });
    works.sort(sortBy('title', true, x => x.toUpperCase()));
    return works;
  },

  async work(urn) {
    const url = `${this.url}?request=GetCapabilities&urn=${urn}`;
    const response = await fetch(url);
    const text = await response.text();
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(text, 'text/xml');
    const select = xpath.useNamespaces({ cts: 'http://chs.harvard.edu/xmlns/cts' });
    const editions = [];
    select('//cts:TextInventory/cts:textgroup/cts:work/cts:edition', xmlDoc).forEach((work) => {
      const workURN = select('@urn', work)[0].textContent;
      const label = select('cts:label', work)[0].textContent;
      editions.push({ urn: workURN, label });
    });
    return editions;
  },

  async edition(urn) {
    const url = `${this.url}?request=GetValidReff&urn=${urn}`;
    const response = await fetch(url);
    const text = await response.text();
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(text, 'text/xml');
    const select = xpath.useNamespaces({ cts: 'http://chs.harvard.edu/xmlns/cts' });
    return select('//cts:reff/cts:urn', xmlDoc)[0].textContent;
  },

  async passage(urn) {
    const url = `http://cts.perseids.org/api/cts/?request=GetPassagePlus&urn=${urn}`;
    const response = await fetch(url);
    const text = await response.text();
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(text, 'text/xml');
    const xsltProcessor = new XSLTProcessor();
    const xslDoc = parser.parseFromString(teiXSL, 'text/xml');
    xsltProcessor.importStylesheet(xslDoc);
    const select = xpath.useNamespaces({ cts: 'http://chs.harvard.edu/xmlns/cts' });
    const fragment = xsltProcessor.transformToFragment(xmlDoc, document);
    const passage = {
      fragment,
      next: select('//cts:prevnext/cts:next/cts:urn', xmlDoc)[0].textContent,
      prev: select('//cts:prevnext/cts:prev/cts:urn', xmlDoc)[0].textContent,
    };
    return passage;
  },

};
