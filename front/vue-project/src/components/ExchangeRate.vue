
<template>
  <div >
      <div ref="gcw_main" id='gcw_mainFIvZA5mnh' class="exchange"></div>
      <!-- <a id='gcw_siteFIvZA5mnh' href='https://freecurrencyrates.com/en/'>FreeCurrencyRates.com</a> -->
  </div>
</template>

<script setup>
import { ref,onMounted } from 'vue'

onMounted(() => {
  reloadFIvZA5mnh()
})

function reloadFIvZA5mnh() {
  console.log(1)
  const sc = document.getElementById('scFIvZA5mnh')
  if (sc) sc.parentNode.removeChild(sc)
  console.log(2)
  let scNew = document.createElement('script')
  scNew.type = 'text/javascript'
  scNew.charset = 'UTF-8'
  scNew.async = true
  scNew.id='scFIvZA5mnh'
  scNew.src = 'https://freecurrencyrates.com/en/widget-vertical?iso=USD-EUR-GBP-JPY-CNY-XUL&df=2&p=FIvZA5mnh&v=fits&source=fcr&width=245&width_title=0&firstrowvalue=1&thm=A6C9E2,FCFDFD,4297D7,5C9CCC,FFFFFF,C5DBEC,FCFDFD,2E6E9E,000000&title=Currency%20Converter&tzo=-540'
  console.log(3)
  const div = document.getElementById('gcw_mainFIvZA5mnh')
  div.parentNode.insertBefore(scNew, div)
  console.log(4)
}
</script>

<style scoped>
.exchange {
  margin-top : 20px;
  margin-left : 200px;
  width :40%;
  height:300px;
}
</style>
