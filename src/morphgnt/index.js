import fetch from 'universal-fetch';

export default {
  apiRoot: 'https://api.morphgnt.org',
  async resource(path) {
    const resp = await fetch(`${this.apiRoot}${path}`);
    return resp.json();
  },
  async books() {
    const { books } = await this.resource('/v0/root.json');
    return books;
  },
  async verseLookup(verse) {
    const url = `${this.apiRoot}/v0/verse-lookup/?${verse}`;
    const resp = await fetch(url);
    const data = await resp.json();
    if (resp.status === 400) {
      throw data.message;
    } else {
      return data.verse_id;
    }
  },
  async frequency(input) {
    const url = `${this.apiRoot}/v0/frequency/`;
    const headers = new Headers({
      'Content-Type': 'application/json',
    });
    const body = JSON.stringify(input);
    const resp = await fetch(url, { method: 'POST', headers, body });
    const data = await resp.json();
    return data.output;
  },
  async kwic(word) {
    const url = `${this.apiRoot}/v0/kwic/?${word}`;
    const resp = await fetch(url);
    const data = await resp.json();
    return data.results;
  },
};
