<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>const{createApp,ref}=Vue
createApp({el:'#app',delimiters:['[[',']]'],setup(){const message=ref('Hello vue!')
return{message}}}).mount('#app');