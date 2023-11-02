const{createApp,ref}=Vue
createApp({el:'#app',delimiters:['[[',']]'],setup(){const message=ref('Hello vue!')
return{message}}}).mount('#app');