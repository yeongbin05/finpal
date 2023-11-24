<template>
  <div>
    
    <div style="background-color: white;" v-if="chartData.labels">
    <Bar
    id="my-chart-id"
    :options="chartOptions"
    :data="chartData"
    
  />
  <h1 style="display:none;">{{ productList }}</h1>
  <!-- <h1>{{ store.zeroArray }}</h1> -->
  <!-- <h1>{{ store.zeroArray }}</h1> -->
  <!-- <h1>11</h1> -->
  <!-- <h1>{{ store.zeroArray }}</h1> -->
</div>
  </div>
</template>

<script setup>

import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

import { onMounted,ref,inject } from 'vue';
import {useRateStore} from '@/stores/rate'
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const chartOptions = ref({
  responsive: true
})

const store = useRateStore()

const productList = store.productList
const finInfosResult = ref([])
const zeroArray = ref(store.zeroArray)
// const zeroArray = ref(Array(38).fill(0))
const chartData = ref({
  labels: [],
  
  datasets: [{ data: store.zeroArray }]
  // datasets: [{ data: [] }]
})
console.log(777)
onMounted(() => {
  console.log(store.zeroArray,29846137)
  console.log(2222)
  store.getFinInfos()
  store.getUserData()
  console.log(`productList : ${productList}`)
  
  for(let i=0;i<productList.length;i++){
  chartData.value.labels.push(productList[i])
}
  console.log('userdata나오신다')
  // console.log(store.userData[0].fields.financial_products)
  // for(let i=0;i<store.userData.length<i++){
  //   if(store.userData[i].fields.financial_products)
  // }
  console.log(chartData.value.labels)
  console.log(`38: ${chartData.value.datasets[0].data}`)
  chartData.value.datasets[0].data[0]=1
  console.log(chartData.value.datasets[0].data)
  // chartData.value.labels.push(1)
  console.log(store.zeroArray,2123124124)



});

</script>
<script>

// import { Bar } from 'vue-chartjs'
// import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

// ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
// console.log(1)
// // console.log(store)
// export default {
  
//   data() {
//     return {
//       chartData: {
//         labels: [ 'January', 'February', 'March' ],
//         datasets: [ { data: [40, 20, 12] } ]
//       },
//       chartOptions: {
//         responsive: true
//       }
//     }
//   }
// }
</script>

<style scoped>
* {
  color:black;
}

</style>