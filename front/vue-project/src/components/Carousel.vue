<template>
  

<div>
  <!-- <div class="custom-carousel">
    <img class='pics' :src="homepics">
    <div>
      <i @click="leftClicked" class="fa-solid fa-chevron-left"></i>
      <i @click="rightClicked" class="fa-solid fa-chevron-right"></i>
    </div>
  </div> -->
  <div id="carouselExample" class="carousel slide">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="https://scontent-ssn1-1.xx.fbcdn.net/v/t1.6435-9/174206810_4024590510935430_3091853476947703323_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=300f58&_nc_ohc=FIiJG7YZ8hkAX_wFx4u&_nc_ht=scontent-ssn1-1.xx&oh=00_AfA36-tXunYOtkIB_kJF3XQ1jtgSPusFFDIGesySQC-HmA&oe=657D186A" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="https://i.ytimg.com/vi/_iqw0ZXBVys/maxresdefault.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="https://cdn.apnews.kr/news/photo/202205/3002388_22677_5152.png" class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
 
</div>
</template>

<script setup>
// import ExchangeRateView from '@/views/ExchangeRateView.vue'
import {RouterView, RouterLink} from 'vue-router'
import {ref} from 'vue'
const pics =ref([
  {
    'pic': 'https://scontent-ssn1-1.xx.fbcdn.net/v/t1.6435-9/174206810_4024590510935430_3091853476947703323_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=300f58&_nc_ohc=FIiJG7YZ8hkAX_wFx4u&_nc_ht=scontent-ssn1-1.xx&oh=00_AfA36-tXunYOtkIB_kJF3XQ1jtgSPusFFDIGesySQC-HmA&oe=657D186A',
    

  },
  {
    'pic' : 'https://i.ytimg.com/vi/_iqw0ZXBVys/maxresdefault.jpg',
    // 'pic' : 'http://www.insidevina.com/news/photo/202307/24515_27416_2842.png',
    
  },
  {
    'pic' : 'https://cdn.apnews.kr/news/photo/202205/3002388_22677_5152.png',
   
  }
  

])

const homepics = ref('https://scontent-ssn1-1.xx.fbcdn.net/v/t1.6435-9/174206810_4024590510935430_3091853476947703323_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=300f58&_nc_ohc=FIiJG7YZ8hkAX_wFx4u&_nc_ht=scontent-ssn1-1.xx&oh=00_AfA36-tXunYOtkIB_kJF3XQ1jtgSPusFFDIGesySQC-HmA&oe=657D186A')
let cn = 0
const leftClicked = function(){
  
  if (cn===0){
    cn = pics.value.length-1
    homepics.value = cn
  }
  else {
    cn-=1
  }
  
  homepics.value = pics.value[cn].pic
 
}
const rightClicked = function(){
  if (cn === pics.value.length-1){
    cn = 0
  }
  else {
    cn+=1
  }
  
  homepics.value = pics.value[cn].pic

}



</script>

<style scoped>
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
  height : 700px;
  
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
</style>