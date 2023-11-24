<template>
    <div>
        <header v-if="language==='한국어'">
        <!-- <a href="#" class="logo">3D</a> -->
        <div class="finance-flex">
      <span><h1>적금 상세</h1></span>
      
    </div>
        <!-- <img src="newyork.png" id="newyork" > -->
        <ul>
            <li><a href="/home" >Home</a></li>
            <li><a href="/FinanceProduct" class="active">금융 상품</a></li>
            <!-- <li><a href="/exchangerate">환율</a></li> -->
            <li><a href="/ex2">환율 2</a></li>
           
        </ul>
    </header>   
        <header v-else>
        <!-- <a href="#" class="logo">3D</a> -->
        <div class="finance-flex">
      <span><h1>Saving Detail</h1></span>
      
    </div>
        <!-- <img src="newyork.png" id="newyork" > -->
        <ul>
            <li><a href="/home" >Home</a></li>
            <li><a href="/FinanceProduct" class="active">Finance Product</a></li>
            <!-- <li><a href="/exchangerate">환율</a></li> -->
            <li><a href="/ex2">Exchange Rate 2</a></li>
           
        </ul>
    </header>   
     
      <div class="custom-title">
        <div  v-for="save in saving" >
            {{save}}
        </div>
   
    </div>
      

      <hr>
      <div v-for="saving in savingDetail">
      {{ saving }}
    </div>
    <button v-if="store.isLogin" @click="addCart(saving,savingDetail)" style="color : black;">
      가입하기
    </button>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios'
  import { onMounted,ref,inject,computed } from 'vue';
  import {useRoute,useRouter} from 'vue-router'
  import {useRateStore} from '@/stores/rate'
  const language = inject('language',ref(''))
  
  const store = useRateStore()
  const route = useRoute()
  const router = useRouter()
  // const products = ref([])
  const saving = ref(null)
  const savingDetail = ref(null)
  onMounted(()=>{
    axios({
      method:'get',
      url : `http://127.0.0.1:8000/fininfos/deposit-products/saving_product/${route.params.id}`
    })
    .then((res)=>{
      saving.value = res.data
      console.log(saving.value.fin_prdt_cd)
  
      axios({
      method:'get',
      url : `http://127.0.0.1:8000/fininfos/deposit-products-options/saving_products/${saving.value.fin_prdt_cd}`
    })
    .then((res)=>{
      console.log(res.data)
      savingDetail.value = res.data
      console.log(res)
      
    })
    .catch(err=>console.log(err))
      
    })
    .catch(err=>console.log(err))
  })
  const productIsEmpty = computed(() => {
  return saving.value.length > 0 ? true : false
})

const addCart = (product,productDetail) => {
  // 하나의 데이터만 저장하기
  // 문제점 : 덮어쓰기 된다.
  // localStorage.setItem('cart', JSON.stringify(product))

  // 여러 데이터 저장하기
  // 현재 localStorage 에 저장된 데이터 가져오기
  // 만약 없다면 비어있는 리스트로 초기화
  const existingCart = JSON.parse(localStorage.getItem('cart')) || []

  // 중복된 제품이 있는지 확인
  const isDuplicate = existingCart.length > 0 && existingCart.find((item) => item.product.fin_prdt_cd === saving.fin_prdt_cd)

  // 중복이 아니라면 추가
  if(!isDuplicate) {
    alert('가입상품에 추가합니다')
    const combinedData = { product,productDetail }
    existingCart.push(combinedData)
  } else {
    alert('이미 있는 상품입니다. 가입상품으로 이동합니다.')
  }

  // 수정된 카트 데이터를 localStorage 에 저장
  localStorage.setItem('cart', JSON.stringify(existingCart))

  router.push('/cart')
}

  </script>
  
  <style scoped>
  * {
    color : white;
  }

  .custom-title {
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

  </style>