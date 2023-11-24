<template>
    <div class="whole">
        <h1>가입상품</h1>
    <div v-if="cartItems && cartItems.length > 0" class="product-list">
      
      <div v-for="product in cartItems" :key="product.id" class="product-card" >
       
        <!-- {{ product }} -->
        <h3>{{ product.product.fin_prdt_cd }}</h3>
        <p>{{ product.product.kor_co_nm }}</p>
        <p>{{ product.product.fin_prdt_nm }}</p>
        <p>{{ product.product.max_limit }}</p>
        <p>{{ product.product.mtrt_int }}</p>
        <p>{{ product.product.spcl_cnd }}</p>
        <p>{{ product.product.etc_note }}</p>
        <!-- <h4>{{ product.productDetail.intr_rate_type_nm }}</h4> -->
        <!-- <h4>{{ product.productDetail.intr_rate }}</h4> -->
        <!-- <h4>{{ product.productDetail.intr_rate2 }}</h4> -->
        <!-- <h4>{{ product.productDetail.save_trm }}</h4> -->
        
        <!-- <button @click="goDetail(product)">상세페이지로 이동</button> -->
        <button @click="removeCart(product)">가입상품에서 삭제</button>
      </div>
      <Bar :options="chartOptions" :data="chartData" v-if="chartData.labels.length > 0" /> 
        
    </div>
    <div v-else>
      <strong>가입하신 상품이 없습니다.</strong>
    </div>
      
    </div>
</template>

<script setup>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import {useRateStore} from '@/stores/rate'
import { onMounted,ref,inject } from 'vue';
import { useRouter } from 'vue-router'
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const router = useRouter()
const store = useRateStore()
// const move = function() {
//   router.push()
// }
const chartOptions = ref({
  responsive: true,
  scales: {
    y: {
      ticks: {
        color: 'white', // y 축의 눈금 글자 색상을 흰색으로 설정
      },
    },
  },
  plugins: {
    legend: {
      labels: {
        color: 'white', // 범례(legend) 글자 색상을 흰색으로 설정
      },
    },
  },
  scales: {
    x: {
      ticks: {
        color: 'white', // x 축 눈금 레이블 색상을 흰색으로 설정
      },
    },
  },
});
const chartData = ref({
  labels: [],
  datasets: [],
});

const cartItems = ref(null)

cartItems.value = JSON.parse(localStorage.getItem('cart'))

// const goDetail = (product) => {
//   router.push(`/${product.id}`)
// }

const removeCart = (product) => {

  const itemIdx = cartItems.value.findIndex((item) => item.id === product.id)

  cartItems.value.splice(itemIdx, 1)
  // console.log(cartItems.value,12512)
  // console.log(cartItems.value[0].product.fin_prdt_nm,12512)
  localStorage.setItem('cart', JSON.stringify(cartItems.value))
  // location.reload()
}
const colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange'];
const getChartData = () => {
  const data = {
    labels: ['저축 금리','최고 우대 금리'],
    datasets: [],
  };

  cartItems.value.forEach((product, index) => {
    // data.labels.push(`int_rate${index + 1}`);
    const backgroundColor = colors[index % colors.length];
    data.datasets.push({
      label: `${cartItems.value[0].product.fin_prdt_nm} `,
      // label: `Product ${index + 1} Interest Rate Comparison`,
      backgroundColor,
      data: [product.productDetail.intr_rate, product.productDetail.intr_rate2],
      
    });
  });

  return data;
};

onMounted(() => {
  chartData.value = getChartData();
});

</script>

<style scoped>
* {
    color: white;
}
.product-card {
    border : 1px solid white;
    padding : 10px;
}
button {
    background-color: black;
}

h1 { 
  margin-top : 110px;
}

.whole {
  margin : 50px;
}
</style>