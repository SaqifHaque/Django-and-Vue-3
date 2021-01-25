import { createApp } from 'vue'
import App from './App.vue'
import router from './configurations/routes.js'

createApp(App).use(router).mount('#app')
