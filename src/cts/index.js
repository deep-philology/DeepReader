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
    const textGroupNode = select('//cts:TextInventory/cts:textgroup', xmlDoc)[0];
    const textGroup = {
      urn: select('@urn', textGroupNode)[0].textContent,
      groupName: select('cts:groupname', textGroupNode)[0].textContent,
    };
    const works = [];
    select('//cts:TextInventory/cts:textgroup/cts:work', xmlDoc).forEach((work) => {
      const workURN = select('@urn', work)[0].textContent;
      const title = select('cts:title', work)[0].textContent;
      works.push({ urn: workURN, title });
    });
    works.sort(sortBy('title', true, x => x.toUpperCase()));
    return { textGroup, works };
  },

  async work(urn) {
    const url = `${this.url}?request=GetCapabilities&urn=${urn}`;
    const response = await fetch(url);
    const text = await response.text();
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(text, 'text/xml');
    const select = xpath.useNamespaces({ cts: 'http://chs.harvard.edu/xmlns/cts' });
    const workNode = select('//cts:TextInventory/cts:textgroup/cts:work', xmlDoc)[0];
    const work = {
      urn: select('@urn', workNode)[0].textContent,
      title: select('cts:title', workNode)[0].textContent,
    };
    const editionFn = async (edition) => {
      const editionURN = select('@urn', edition)[0].textContent;
      const label = select('cts:label', edition)[0].textContent;
      const description = select('cts:description', edition)[0].textContent;
      const firstPassageURN = await this.firstPassage(editionURN);
      return {
        urn: editionURN,
        label,
        description,
        firstPassageURN,
      };
    };
    const results = [];
    select('//cts:TextInventory/cts:textgroup/cts:work/cts:edition', xmlDoc).forEach((edition) => {
      results.push(editionFn(edition));
    });
    const editions = await Promise.all(results);
    return { work, editions };
  },

  async edition(urn) {
    const parser = new DOMParser();
    const select = xpath.useNamespaces({ cts: 'http://chs.harvard.edu/xmlns/cts' });

    const url = `${this.url}?request=GetCapabilities&urn=${urn}`;
    const response = await fetch(url);
    const text = await response.text();
    const xmlDoc = parser.parseFromString(text, 'text/xml');
    const editionNode = select('//cts:TextInventory/cts:textgroup/cts:work/cts:edition', xmlDoc)[0];
    const edition = {
      urn: select('@urn', editionNode)[0].textContent,
      label: select('cts:label', editionNode)[0].textContent,
      description: select('cts:description', editionNode)[0].textContent,
      firstPassageURN: await this.firstPassage(urn),
    };

    return { edition };
  },

  async firstPassage(editionURN) {
    const parser = new DOMParser();
    const select = xpath.useNamespaces({ cts: 'http://chs.harvard.edu/xmlns/cts' });
    const url = `${this.url}?request=GetValidReff&urn=${editionURN}`;
    const response = await fetch(url);
    const text = await response.text();
    const xmlDoc = parser.parseFromString(text, 'text/xml');
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
