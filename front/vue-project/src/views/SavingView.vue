<template>
  <div v-if="language==='한국어'" class="whole">
    
    
    <header>
        <!-- <a href="#" class="logo">3D</a> -->
        <div class="finance-flex">
      <span><h1>금융 상품</h1></span>
      <span ><RouterLink :to="{ name: 'FinanceProduct', params: { page_pk: 1 } } " >예금</RouterLink></span>
      <span><RouterLink :to="{name: 'saving'}" >적금</RouterLink></span>
    </div>
        <!-- <img src="newyork.png" id="newyork" > -->
        <ul>
            <li><a href="/home" >Home</a></li>
            <li><a href="/FinanceProduct/1" class="active">금융 상품</a></li>
            <!-- <li><a href="/exchangerate">환율</a></li> -->
            <li><a href="/ex2">환율 2</a></li>
            <li><a class="nav-link" href="/articles">커뮤니티</a></li>

        </ul>
    </header>
  
    <select v-model="selected">
      <option  value="">은행</option>
      <option >국민</option>
      <option >하나</option>
      <option >신한</option>
      <option >우리</option>
      <option >농협</option>
      <option >스탠다드</option>
      <option >대구</option>
      <option >부산</option>
      <option >광주</option>
      <option >제주</option>
      <option >전북</option>
      <option >경남</option>
      <option >중소</option>
      <option >산업</option>
      <option >신한</option>
      <option >케이뱅크</option>
      <option >수협</option>
      <option >카카오</option>
      <option >토스</option>
    </select>
    <select v-model="selected2">
      <option disabled value="">저축기간</option>
      <option >6</option>
      <option >12</option>
      <option >24</option>
      <option >36</option>
      
    </select>
    <h2>적금</h2>
    <div class="Flex">
    <div class="product-component">금융상품코드</div>
    <div class="product-component">금융회사명</div>
    <div class="product-component">저축금리</div>
    <div class="product-component">최고우대금리</div>
    <div class="product-component">저축기간(단위:개월)</div>
    <div class="product-component">금융상품명</div>
    </div>
    <div v-if="store.finSavingInfosOptions" v-for="(finsavinginfo, index) in finSavingInfosResult" :key="index" class="product-flex lists">
          <div v-if="finsavinginfo.kor_co_nm.includes(selected)" class="Flex">
          <div class="product-component">{{ finsavinginfo.fin_prdt_cd }}</div>
          <div class="product-component">{{ finsavinginfo.kor_co_nm }}</div>
          <div class="product-component">{{ store.finSavingInfosOptions[index].intr_rate }}</div>
          <div class="product-component">{{ store.finSavingInfosOptions[index].intr_rate2 }}</div>
          <div class="product-component">{{ store.finSavingInfosOptions[index].save_trm }}</div>

          <div class="product-component">
            <RouterLink :to="{name:'savingdetail',params:{id:index+1}}">{{ finsavinginfo.fin_prdt_nm }}</RouterLink>
          </div>
          
        </div>
        
        </div>
        
        <nav class="custom-flex" aria-label="Page navigation example">
        <ul class="pagination">
  
    <li class="page-item"><a class="page-link" href="/savings/1">1</a></li>
    <li class="page-item"><a class="page-link" href="/savings/2">2</a></li>
    <li class="page-item"><a class="page-link" href="/savings/3">3</a></li>
    <li class="page-item"><a class="page-link" href="/savings/4">4</a></li>
    <li class="page-item"><a class="page-link" href="/savings/5">5</a></li>
    <li class="page-item"><a class="page-link" href="/savings/6">6</a></li>
    <li class="page-item"><a class="page-link" href="/savings/7">7</a></li>
 
  </ul>
</nav>
  </div>
  <div v-else>
    
    <header>
      
        <div class="finance-flex">
      <span><h1>Products</h1></span>
      <span><RouterLink :to="{name: 'FinanceProduct'}" >Deposit</RouterLink></span>
      <span><RouterLink :to="{name: 'saving'}" >Saving</RouterLink></span>
    </div>
      
        <ul>
            <li><a href="/home" >Home</a></li>
            <li><a href="/FinanceProduct" class="active">Products</a></li>
    
            <li><a href="/ex2">Exchange Rate 2</a></li>
           
        </ul>
    </header>
  
    <select v-model="selected">
      <option disabled value="">Select</option>
      <option >KB</option>
      <option >Hana</option>
      <option >Shinhan</option>
      <option >Woori</option>
      <option >NH</option>
    </select>
    <h2>Saving</h2>
    <div v-for="(finsavinginfo, index) in finSavingInfosResult" :key="index" class="product-flex lists">
          <div v-if="finsavinginfo.kor_co_nm.includes(selected)" class="Flex">
          <div class="product-component">{{ finsavinginfo.fin_prdt_cd }}</div>
          <div class="product-component">{{ finsavinginfo.kor_co_nm }}</div>
          <!-- <div class="product-component">{{ finsavinginfo.fin_prdt_nm }}</div> -->
          <div class="product-component">
            <RouterLink :to="{name:'savingdetail',params:{id:index+1}}">{{ finsavinginfo.fin_prdt_nm }}</RouterLink>
          </div>
          
        </div>
        
        </div>
        <ul class="pagination">
    <!-- <li class="page-item"><a class="page-link" href="#">Previous</a></li> -->
    <li class="page-item"><a class="page-link" href="/savings/1">1</a></li>
    <li class="page-item"><a class="page-link" href="/savings/2">2</a></li>
    <li class="page-item"><a class="page-link" href="/savings/3">3</a></li>
    <li class="page-item"><a class="page-link" href="/savings/4">4</a></li>
    <li class="page-item"><a class="page-link" href="/savings/5">5</a></li>
    <li class="page-item"><a class="page-link" href="/savings/6">6</a></li>
    <li class="page-item"><a class="page-link" href="/savings/7">7</a></li>
    <!-- <li class="page-item"><a class="page-link" href="#">Next</a></li> -->
  </ul>
  </div>
</template>

<script setup>
import { onMounted,ref,inject } from 'vue';

import {useRateStore} from '@/stores/rate'
const store = useRateStore()
const finInfosResult = ref([])
const finSavingInfosResult = ref([])
const selected = ref(0)
const selected2 = ref(0)
const language = inject('language',ref(''))
const fetchSavingData = async () => {
  try {
    await store.getFinSavingInfos();
    console.log(34345)
    console.log(store.getFinSavingInfos)
    finSavingInfosResult.value = store.finSavingInfosResult;
    console.log(finSavingInfosResult.value);
  } catch (error) {
    console.error(error);
  }
};
onMounted(() => {
  console.log('onMounted is called1');
  selected.value=''
  selected2.value=''
  fetchSavingData()
});
</script>

<style scoped>

select {
  margin-top: 130px;
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
    margin-top: 20px;
    
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
h1,h2 {
  color : #fff;
}
.lists {
  
  backdrop-filter: blur(8px);
  background-color: rgba(255, 255, 255, 0.5);
  opacity: 1;

}
.Flex {
  display : flex;
  width : 100%;
}
.product-flex {
  display : flex;
}
.product-component {
  border : 1px solid lightgrey;
  width : 33%;
  text-align: center;
  color:white;
}

.ye-juk {
  display : flex;
  
}

.ye-juk > div {
  width : 50%;
}
.finance-flex {
  display : flex;

}

.finance-flex > span {
  margin-left : 20px;
  font-size : 30px;
}
.custom-flex {
  display : flex;
  justify-content: center;
  margin-top : 20px;
  

}

.pagination > li >a {
  backdrop-filter: blur(8px);
  background-color: rgba(255, 255, 255, 0.5);
  opacity: 1;
}

.whole {
  padding : 20px;
}

</style>