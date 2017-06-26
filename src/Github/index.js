import fetch from 'universal-fetch';

export default {
  apiRoot: 'https://api.github.com',
  async resource(path) {
    const resp = await fetch(`${this.apiRoot}${path}`);
    return resp.json();
  },
  async issues() {
    const url = '/repos/deep-reader/DeepReader/issues';
    const resp = await this.resource(url);
    return resp;
  },
};
