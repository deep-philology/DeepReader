import firebase from 'firebase';

const config = {
  apiKey: 'AIzaSyAOCV-UXcEChFFw5G2SBigve8hClyJhnk8',
  authDomain: 'lore-cb5e2.firebaseapp.com',
  databaseURL: 'https://lore-cb5e2.firebaseio.com',
  projectId: 'lore-cb5e2',
  storageBucket: 'lore-cb5e2.appspot.com',
  messagingSenderId: '1072950462053',
};

export default firebase.initializeApp(config);
