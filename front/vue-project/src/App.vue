<template>
  <div>
    
    <div class="nav-login-signup" v-if="store.isLogin">
      <span v-if="language==='한국어'">
        <RouterLink :to="{name:'ProfileView'}">프로필</RouterLink>
        |
        <a href="#" @click.prevent="store.logOut">로그아웃</a>
      </span>
      <span v-else>
        <RouterLink :to="{name:'ProfileView'}">Profile</RouterLink>
         |
        <a href="#" @click.prevent="store.logOut">Logout</a>
        </span>
      
        <!-- <span v-if="language==='한국어'">
        <RouterLink :to="{name:'SignUp'}">회원가입</RouterLink>
      </span>
      <span v-else>
        <RouterLink :to="{name:'SignUp'}">SignUp</RouterLink>

      </span> -->

      <select v-model="language" @change="saveLanguage">
        <option >한국어</option>
        <option >english</option>
      </select>     
      
    </div>
    
    <div class="nav-login-signup" v-else>
      <!-- <span v-if="language==='한국어'">
        <RouterLink :to="{name:'LogIn'}">로그인</RouterLink>
      </span>
      <span v-else>
          <RouterLink :to="{name:'LogIn'}">Login</RouterLink>
        </span> -->

        <div class="dropdown">
          <img src="src\assets\user-profile (1).png" alt="Your Image" @click="toggleDropdown" style="cursor: pointer; height: 40px; margin-right: 10px;" >
          <div v-if="isDropdownVisible" class="dropdown-menu">
            <span v-if="language==='한국어'">
              <a class="dropdown-item" href="/login">로그인</a>
              <a class="dropdown-item" href="/signup">회원가입</a>
          </span>
          <span v-else>
            <a class="dropdown-item" href="/login">Login</a>
            <a class="dropdown-item" href="/signup">Sign</a>
          </span>
          </div>
        </div>
      
        <!-- <span v-if="language==='한국어'">
        <RouterLink :to="{name:'SignUp'}">회원가입</RouterLink>
      </span>
      <span v-else>
        <RouterLink :to="{name:'SignUp'}">SignUp</RouterLink> -->

      <select v-model="language" @change="saveLanguage">
        <option >한국어</option>
        <option >english</option>
      </select>     
      
    </div>

  </div>
  

        
  <RouterView />
</template>

<script setup>
import { onMounted,ref,provide } from 'vue';
import { useRateStore } from '@/stores/rate'

const language = ref('')
const store = useRateStore()
const isDropdownVisible = ref(false)

const toggleDropdown = () => {
    isDropdownVisible.value = !isDropdownVisible.value;
  }

provide('language',language)
onMounted(()=>{
  language.value = localStorage.getItem('selectedLanguage') || '한국어'
})
const saveLanguage = function() {
  localStorage.setItem('selectedLanguage', language.value);
  console.log(language)
}
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900&display=swap');
*
{
    margin:0;
    padding:0;
    box-sizing: border-box;
    font-family: 'Poppins',sans-serif;
    scroll-behavior: smooth;
}
.language {
  color: white;
}
span {
  margin : 10px 10px 0 0;
}
.logo {
  width: 50px;

}
.nav-login-signup {
  position : absolute;
  right : 40px;
  top : 10px;
  display : flex;
  justify-content: flex-end;
  z-index : 6000;
  margin-bottom: 20px;
}


  .home-2 {
    display : flex;
    justify-content: center;
    align-items: center;
    width : 100%;
  }
  
  .custom-nav {
    display : flex;
    justify-content: center;
    align-items: center;
  }
  .notice > p {
    margin :0 ;
  }
  .notice { 
    background-color: beige;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .custom-carousel {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .pics {
    width : 100%;
    
    
  }
  .container {
    display : flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    background-color:#F1F5F8;
    height:700px;
    font-weight: bold;
  
  }
  
  .title {
    font-size: 50px;
    color : #0B263D;
  }
  
  .content {
    background-color: white;
    width:80%;
    height: 500px;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    align-items: center;
  } 
  
  .line  {
    background-color: #47A4EA;
    height:0.5rem;
    width:5rem;
  }
  
  .top { 
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  /* 
  img {
    width:150px;
    height:150px;
    border-radius: 50%;
  } */
  
  i {
    margin-right: 20px;
  }
  /* .custom-nav {
    
    display : flex;
    justify-content: space-between;
    align-items: center;
  } */




body {
    min-height: 100vh;
    overflow-x : hidden;
    background: linear-gradient(#2b1055,#7597de);
}

/* #kb {
    position: absolute;
    left: 0; /* 초기 위치를 0으로 설정하거나 필요에 따라 조절하세요 */
    /* 그 외의 스타일 속성들... 
} */

header {
    position: absolute;
    top : 0;
    left:0;
    width : 100%;
    padding : 30px 100px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index : 10000
}

header .logo{
    color : #fff;
    font-weight: 700;
    text-decoration: none;
    font-size : 2em;
    text-transform: uppercase;
    letter-spacing: 2px;
}

header ul {
    display : flex;
    justify-content: center;
    align-items: center;
}

header ul li{
    list-style: none;
    margin-left: 20px;
}
/* #newyork { 
    width : 30px;
    height : 30px;
} */
header ul li a {
    text-decoration: none;
    padding : 6px 15px;
    color : #fff;
    border-radius: 20px;
}

header ul li a:hover, header ul li a.active
 {
    background: #2196f3;
    color : #255784;
    box-shadow : 0 0 10px #2196f3, 0 0 40px #2196f3, 0 0 80px #2196f3;
}
/* header ul li a:hover, header ul li a.active
 {
    background: #fff;
    color : #2b1055
} */

section {
    position : relative;
    width : 100%;
    height : 100vh;
    padding: 100px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
}
section::before
{
    content : '';
    position : absolute;
    bottom : 0;
    width : 100%;
    height : 100px;
    background: linear-gradient(to top,#1c0522,transparent);
    z-index:1000;
}
section img {
   
    position : absolute;
    right : 350px;
    color :#fff;
    white-space: nowrap;
    font-size : 7.5vw;
    z-index: 9;
}

section img#moon {
    mix-blend-mode: screen;
}

section img#mountains_front {
    z-index : 10;
}
#text {
    position : absolute;
    top : 0;
    left: 0;
    width : 100%;
    height: 100%;
    object-fit: cover;
    pointer-events: none;
    
}
#uri {
    top : 100px;
}

#nh {
    top : 300px;
}
#btn {
    text-decoration: none;
    display : inline-block;                            
    padding : 8px 30px;
    border-radius: 40px;
    background: #fff;
    color : #2b1055;
    font-size : 1.5em;
    z-index: 9;
    transform: translateY(100px);
}

.sec {
    position : relative;
    padding : 100px;
    background : #1c0522;
}

.sec h2 {
    font-size : 3.5em;
    margin-bottom: 10px;
    color :#fff;
}

.sec p {
    font-size : 1.2em;
    color:#fff;
}
  </style>
  <style>
  @import url('https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800,900&display=swap');
*
{
  margin:0;
  padding:0;
  box-sizing: border-box;
  font-family: 'Poppins',sans-serif;
  scroll-behavior: smooth;
}
span {
margin : 10px 10px 0 0;
}
.logo {
width: 50px;

}
.nav-login-signup {
display : flex;
justify-content: flex-end;
}


.home-2 {
  display : flex;
  justify-content: center;
  align-items: center;
  width : 100%;
}

.custom-nav {
  display : flex;
  justify-content: center;
  align-items: center;
}
.notice > p {
  margin :0 ;
}
.notice { 
  background-color: beige;
  display: flex;
  justify-content: center;
  align-items: center;
}
.custom-carousel {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.pics {
  width : 100%;
  
  
}
.container {
  display : flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  background-color:#F1F5F8;
  height:700px;
  font-weight: bold;

}

.title {
  font-size: 50px;
  color : #0B263D;
}

.content {
  background-color: white;
  width:80%;
  height: 500px;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
} 

.line  {
  background-color: #47A4EA;
  height:0.5rem;
  width:5rem;
}

.top { 
  display: flex;
  flex-direction: column;
  align-items: center;
}
/* 
img {
  width:150px;
  height:150px;
  border-radius: 50%;
} */

i {
  margin-right: 20px;
}
/* .custom-nav {
  
  display : flex;
  justify-content: space-between;
  align-items: center;
} */




body {
  min-height: 100vh;
  overflow-x : hidden;
  background: linear-gradient(#2b1055,#7597de);
}

/* #kb {
  position: absolute;
  left: 0; /* 초기 위치를 0으로 설정하거나 필요에 따라 조절하세요 */
  /* 그 외의 스타일 속성들... 
} */

header {
  position: absolute;
  top : 0;
  left:0;
  width : 100%;
  padding : 30px 100px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index : 10000
}

header .logo{
  color : #fff;
  font-weight: 700;
  text-decoration: none;
  font-size : 2em;
  text-transform: uppercase;
  letter-spacing: 2px;
}

header ul {
  display : flex;
  justify-content: center;
  align-items: center;
}

header ul li{
  list-style: none;
  margin-left: 20px;
}
/* #newyork { 
  width : 30px;
  height : 30px;
} */
header ul li a {
  text-decoration: none;
  padding : 6px 15px;
  color : #fff;
  border-radius: 20px;
}

header ul li a:hover, header ul li a.active
{
  background: #2196f3;
  color : #255784;
  box-shadow : 0 0 10px #2196f3, 0 0 40px #2196f3, 0 0 80px #2196f3;
}
/* header ul li a:hover, header ul li a.active
{
  background: #fff;
  color : #2b1055
} */

section {
  position : relative;
  width : 100%;
  height : 100vh;
  padding: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}
section::before
{
  content : '';
  position : absolute;
  bottom : 0;
  width : 100%;
  height : 100px;
  background: linear-gradient(to top,#1c0522,transparent);
  z-index:1000;
}
section img {
 
  position : absolute;
  right : 350px;
  color :#fff;
  white-space: nowrap;
  font-size : 7.5vw;
  z-index: 9;
}

section img#moon {
  mix-blend-mode: screen;
}

section img#mountains_front {
  z-index : 10;
}
#text {
  position : absolute;
  top : 0;
  left: 0;
  width : 100%;
  height: 100%;
  object-fit: cover;
  pointer-events: none;
  
}
#uri {
  top : 100px;
}

#nh {
  top : 300px;
}
#btn {
  text-decoration: none;
  display : inline-block;                            
  padding : 8px 30px;
  border-radius: 40px;
  background: #fff;
  color : #2b1055;
  font-size : 1.5em;
  z-index: 9;
  transform: translateY(100px);
}

.sec {
  position : relative;
  padding : 100px;
  background : #1c0522;
}

.sec h2 {
  font-size : 3.5em;
  margin-bottom: 10px;
  color :#fff;
}

.sec p {
  font-size : 1.2em;
  color:#fff;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-menu {
  height: 100px;
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 130px;
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-menu a {
  padding: 12px 16px;
  display: block;
  text-decoration: none;
  color: #333;
}

.dropdown-menu a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-menu {
  display: block;
}
</style>
