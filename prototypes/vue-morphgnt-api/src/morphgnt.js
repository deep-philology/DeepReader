import axios from 'axios';

export default {
  // apiRoot: 'https://api.morphgnt.org',
  apiRoot: 'http://localhost:8000',
  async resource(path) {
    const { data: resource } = await axios.get(`${this.apiRoot}${path}`);
    return resource;
  },
  async books() {
    const { books } = await this.resource('/v0/root.json');
    return books;
  },
  async verseLookup(verse) {
    const url = `${this.apiRoot}/v0/verse-lookup/?${verse}`;
    const response = await axios.get(url, { validateStatus: null });
    if (response.status === 400) {
      throw response.data.message;
    } else {
      return response.data.verse_id;
    }
  },
  async frequency(input) {
    const url = `${this.apiRoot}/v0/frequency/`;
    const response = await axios.post(url, { input }, { validateStatus: null });
    return response.data.output;
  },
};
