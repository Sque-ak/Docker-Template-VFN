import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import axios from 'axios';

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/'; // FastAPI Backend

createApp(App).use(router).mount('#app')
