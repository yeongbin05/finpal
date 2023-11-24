<template>
  <div v-if="language==='한국어'">
    <header>
        <!-- <a href="#" class="logo">3D</a> -->
        <div style="font-size:30px; color : white;">환율 계산기</div>
        <!-- <img src="newyork.png" id="newyork" > -->
        <ul>
            <li><a href="/home" >Home</a></li>
            <li><a href="/FinanceProduct/1" >금융 상품</a></li>
            <!-- <li><a href="/exchangerate">환율</a></li> -->
            <li><a href="/ex2" class="active">환율 2</a></li>
            <li><a class="nav-link" href="/articles">커뮤니티</a></li>

           
        </ul>
    </header>
<h1>환율 계산기</h1>
<div class="up-input">
<select @click="click" v-model="selected"  style="text-align: center;">
  <option v-for="(rate, index) in store.ratesResult" :key="index">{{ rate.CUR_NM }}</option>
  
</select>

<input type="text" v-model="price" :placeholder="resultPrice2" @input ="cal" style="text-align: end;">
</div>
<input class="bottom-input" type="text" v-model="price2" :placeholder="resultPrice" @input="cal2" style="text-align: end;">원
<hr>


<div v-for="(rate, index) in store.ratesResult" :key="index">
  {{ rate.CUR_NM }} {{ rate.BKPR }}/1
</div>
<!-- {{ ratesResult }} -->

  </div>
  <div v-else>
    <header>
        <!-- <a href="#" class="logo">3D</a> -->
        <div style="font-size:30px; color : white;">Exchange Rate Calculate</div>
        <!-- <img src="newyork.png" id="newyork" > -->
        <ul>
            <li><a href="/home" >Home</a></li>
            <li><a href="/FinanceProduct" >Products</a></li>
            <!-- <li><a href="/exchangerate">Exchange Rate</a></li> -->
            <li><a href="/ex2" class="active">Exchange Rate 2</a></li>
           
        </ul>
    </header>
<h1>Exchange Rate Calculate</h1>
<select @click="click" v-model="selected"  >
  <option v-for="(rate, index) in store.ratesResult" :key="index">{{ rate.CUR_NM }}</option>
  
</select>
<!-- {{ selected }} -->
<input type="text" v-model="price" @input ="cal"  >

<input type="text" :placeholder="resultPrice">Won

<div v-for="(rate, index) in store.ratesResult" :key="index">
  {{ rate.CUR_NM }} {{ rate.BKPR }}/1
</div>
  </div>
</template>

<script setup>
import { onMounted,ref,inject } from 'vue';
import {useRateStore} from '@/stores/rate'
const click = function (){
  price.value=''
  resultPrice.value=''
}
const click2 = function (){
  price2.value=''
  resultPrice2.value=''
}
const store = useRateStore()
const ratesResult = ref('')
const selected = ref('')
const price = ref('')
const price2 = ref('')
const resultPrice = ref('')
const resultPrice2 = ref('')
const language = inject('language',ref(''))
// const ratesResultProxy = store.ratesResult
const cal = function () {
  
  for ( let i =0;i<store.ratesResult.length;i++){
    
    if ( selected.value  === store.ratesResult[i].CUR_NM) {
     
      
      let res= store.ratesResult[i].DEAL_BAS_R.split('.')[0]
      let Res = ''
      if (res.includes(',')){
        
        Res = res.split(',').join('')
        
      }
      else {
        Res = res
      }
      
      
      if (store.ratesResult[i].CUR_UNIT.includes('100')){
        resultPrice.value = Res * parseInt(price.value)/100
      }
      else {
      resultPrice.value = Res * parseInt(price.value)
      }
      
    }

  }
    

}
const cal2 = function () {
  
  for ( let i =0;i<store.ratesResult.length;i++){
    
    if ( selected.value  === store.ratesResult[i].CUR_NM) {
     
      
      let res= store.ratesResult[i].DEAL_BAS_R.split('.')[0]
      let Res = ''
      if (res.includes(',')){
        
        Res = res.split(',').join('')
        
      }
      else {
        Res = res
      }
      console.log(resultPrice2.value,41)
      
      if (store.ratesResult[i].CUR_UNIT.includes('100')){
        resultPrice2.value = parseInt(price2.value) / Res 
      }
      else {
      resultPrice2.value = parseInt(price2.value)/Res 
      }
      
    }

  }
    

}


const fetchData = () => {
  try {
    store.getRates();
    console.log(3434)  
    
    ratesResult.value = store.ratesResult;
    console.log(ratesResult.value)
  } catch (error) {
    console.error(error);
  }
};
onMounted(() => {
  console.log('onMounted is called');
  fetchData();
});
</script>

<style scoped>
* {
  color : white;
}
h1 {
  color : white;
  margin-top: 120px;
}

header {
    position: absolute;
    top : 0;
    left:0;
    width : 100%;
    padding : 30px 100px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index : 3000;
    padding-left:0px;
    margin-top: 30px;
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

select,option,input {
  color : black;
}

.up-input {
  display : flex;
}
.up-input > select {
  width : 30%;
}
.up-input > input { 
  width :50%;
}

.bottom-input {
  width : 80%;
  margin-top : 30px;
}
</style>