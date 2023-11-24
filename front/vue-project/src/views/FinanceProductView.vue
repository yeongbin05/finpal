<template>
  <div v-if="language==='한국어'" class="whole">
    <header>
        <!-- <a href="#" class="logo">3D</a> -->
        <div class="finance-flex">
      <span><h1>금융 상품</h1></span>
      <span><RouterLink :to="{name: 'FinanceProduct'}" style="color:white;">예금</RouterLink></span>
      <span><RouterLink :to="{name: 'saving'}" style="color:white;">적금</RouterLink></span>
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
    
    <!-- {{ finInfosResult }}
    {{ a }}
    
    <div v-for="(fininfo,index) in finInfosResult" :key="index">
      {{ fininfo }}
    </div> -->
    
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
    
      
      <h2 >예금</h2>
      <!-- {{ store.finInfosOptions[0].save_trm }} -->
      <!-- <div v-if="store.finInfosOptions[0]" >
  {{ store.finInfosOptions[0].intr_rate }}
</div> -->
      <div v-if="store.finInfosOptions">
      
    </div>
    <div v-else>
      없음
    </div>
      <div class="Flex">
    <div class="product-component">금융상품코드</div>
    <div class="product-component">금융회사명</div>
    <div class="product-component">저축금리</div>
    <div class="product-component">최고우대금리</div>
    <div class="product-component">저축기간(단위:개월)</div>
    <div class="product-component">금융상품명</div>
    </div>
        <div v-if="store.finInfosOptions" v-for="(fininfo, index) in finInfosResult" :key="index" class="product-flex lists">
          <!-- <div v-if="store.finInfosOptions[index].save_trm==selected2" class="Flex"> -->
          <!-- <div v-if="fininfo.kor_co_nm.includes(selected)&&(store.finInfosOptions[index].save_trm.includes(selected2))" class="Flex"> -->
        
          <!-- <div v-if="fininfo.kor_co_nm.includes(selected)||(store.finInfosOptions[index].save_trm==selected2)" class="Flex"> -->
            <div class="Flex" v-if="selected===selected2">
              
            <div class="product-component">{{ fininfo.fin_prdt_cd }}</div>
            <div class="product-component">{{ fininfo.kor_co_nm }}</div>
            <div class="product-component">{{ store.finInfosOptions[index].intr_rate }}</div>
            <div class="product-component">{{ store.finInfosOptions[index].intr_rate2 }}</div>
            <div class="product-component">{{ store.finInfosOptions[index].save_trm }}</div>
            
            <!-- <div class="product-component">{{ store.finInfosOption.value[index] }}</div> -->
            <!-- <RouterLink :to="{name:'detail',params:{id:index+1}}">{{ fininfo.kor_co_nm }}</RouterLink> -->

            <!-- <div class="product-component">{{ fininfo.fin_prdt_nm }}</div> -->
            <div class="product-component">
              <RouterLink :to="{name:'detail',params:{id:index+1}}" style="color:white;">{{ fininfo.fin_prdt_nm }}</RouterLink>
            </div>
        </div>
        <div class="Flex" v-else-if="(selected!=0&&selected2!=0)">
          <div class="Flex" v-if="fininfo.kor_co_nm.includes(selected)&&(store.finInfosOptions[index].save_trm==selected2)">
          
          <div class="product-component">{{ fininfo.fin_prdt_cd }}</div>
            <div class="product-component">{{ fininfo.kor_co_nm }}</div>
            <div class="product-component">{{ store.finInfosOptions[index].intr_rate }}</div>
            <div class="product-component">{{ store.finInfosOptions[index].intr_rate2 }}</div>
            <div class="product-component">{{ store.finInfosOptions[index].save_trm }}</div>
            <div class="product-component">
              <RouterLink :to="{name:'detail',params:{id:index+1}}">{{ fininfo.fin_prdt_nm }}</RouterLink>
            </div>
          </div>
        </div>
        <div class="Flex" v-else-if="fininfo.kor_co_nm.includes(selected)||(store.finInfosOptions[index].save_trm==selected2)">
          
          <div class="product-component">{{ fininfo.fin_prdt_cd }}</div>
            <div class="product-component">{{ fininfo.kor_co_nm }}</div>
            <div class="product-component">{{ store.finInfosOptions[index].intr_rate }}</div>
            <div class="product-component">{{ store.finInfosOptions[index].intr_rate2 }}</div>
            <div class="product-component">{{ store.finInfosOptions[index].save_trm }}</div>
            <div class="product-component">
              <RouterLink :to="{name:'detail',params:{id:index+1}}">{{ fininfo.fin_prdt_nm }}</RouterLink>
            </div>
        </div>
      
          
          
        
        </div>
        <nav class="custom-flex" aria-label="Page navigation example">
  <ul class="pagination">
    <!-- <li class="page-item"><a class="page-link" href="#">Previous</a></li> -->
    <li class="page-item"><a class="page-link" href="/financeproduct/1">1</a></li>
    <li class="page-item"><a class="page-link" href="/financeproduct/2">2</a></li>
    <li class="page-item"><a class="page-link" href="/financeproduct/3">3</a></li>
    <li class="page-item"><a class="page-link" href="/financeproduct/4">4</a></li>
    <!-- <li class="page-item"><a class="page-link" href="#">Next</a></li> -->
  </ul>
</nav>
       
    
  </div>
  <div v-else>
    <header>
        <!-- <a href="#" class="logo">3D</a> -->
        <div class="finance-flex">
      <span><h1>Products</h1></span>
      <span><RouterLink :to="{name: 'FinanceProduct'}" >Deposit</RouterLink></span>
      <span><RouterLink :to="{name: 'saving'}" >Saving</RouterLink></span>
    </div>
        <!-- <img src="newyork.png" id="newyork" > -->
        <ul>
            <li><a href="/home" >Home</a></li>
            <li><a href="/FinanceProduct/1" class="active">Products</a></li>
            <!-- <li><a href="/exchangerate">Exchange Rate</a></li> -->
            <li><a href="/ex2">Exchange Rate 2</a></li>
            <li><a class="nav-link" href="/articles">Community</a></li>
           
        </ul>
    </header>
    
    <!-- {{ finInfosResult }}
    {{ a }}
    
    <div v-for="(fininfo,index) in finInfosResult" :key="index">
      {{ fininfo }}
    </div> -->
    
    <select v-model="selected">
      <option disabled value="">Select</option>
      <option >KB</option>
      <option >Hana</option>
      <option >Shinhan</option>
      <option >Woori</option>
      <option >NH</option>
    </select>
    
      
      <h2 >Deposit</h2>
        <div v-for="(fininfo, index) in finInfosResult" :key="index" class="product-flex lists">
          <div v-if="fininfo.kor_co_nm.includes(selected)" class="Flex">
            <div class="product-component">{{ fininfo.fin_prdt_cd }}</div>
            <div class="product-component">{{ fininfo.kor_co_nm }}</div>
            <div class="product-component">
              <RouterLink :to="{name:'detail',params:{id:index+1}}">{{ fininfo.fin_prdt_nm }}</RouterLink>
            </div>
            
        </div>
      
          
          
        
        </div>
        

  </div>
  <RouterView />
</template>

<script setup>
import { onMounted,ref,inject } from 'vue';
import {RouterLink,RouterView } from 'vue-router'
import {useRoute,useRouter} from 'vue-router'
import {useRateStore} from '@/stores/rate'
import axios from 'axios'
const store = useRateStore()
const finInfosResult = ref([])
const finInfosOptions =ref([])
const finSavingInfosResult = ref([])
const page = ref(0)
const selected = ref(0)
const selected2 = ref(0)
const language = inject('language',ref(''))
const product = ref(null)
const productDetail = ref(null)
const route = useRoute()


// console.log(Array.isArray(store.finInfosOptions[0].intr_rate,123123))
const fetchData = async () => {
  try {
    await store.getFinInfos();
    finInfosOptions.value = store.finInfosOptions
    // console.log(finInfosOptions.value,123123424)
    finInfosResult.value = store.finInfosResult
    // console.log(finInfosResult.value,41345132)
    
  } catch (error) {
    console.error(error);
  }
};
const fetchSavingData = async () => {
  try {
    await store.getFinSavingInfos();
    
    finSavingInfosResult.value = store.finSavingInfosResult;
  
  } catch (error) {
    console.error(error);
  }
};
onMounted(() => {
  selected.value=''
  selected2.value=''
  fetchData()
  fetchSavingData()
  
});
console.log(store.finInfosOptions[0],33)
console.log(store.finInfosResult)
// page = 
</script>

<style scoped>
* {
  color:black;
}
select {
  margin-top: 140px;
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


h2 {
  color : #fff;
}
.lists {
  backdrop-filter: blur(8px);
  background-color: rgba(255, 255, 255, 0.2);
  opacity: 1;
}
h1 {
  color : #fff;
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
  color : white;
  height : 45px;
  display : flex;
  justify-content: center;
  align-items: center;
  
}

.ye-juk {
  display : flex;
  
}

.ye-juk > div {
  width : 50%;
}
.finance-flex {
  display : flex;
  /* margin-top: 140px; */
  z-index : 3000;

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