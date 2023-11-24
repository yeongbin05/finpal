import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRoute,useRouter } from 'vue-router'

export const useRateStore = defineStore('rate', () => {
  const router = useRouter()
  const route = useRoute()
  const ratesResult = ref([])
  const finInfosResult = ref([])
  const finInfosOptions = ref([])
  const finSavingInfosResult = ref([])
  const finSavingInfosOptions = ref([])
  const token = ref(null)
  const userId = ref(null)
  const articles = ref([])
  const comments = ref([])
  const userInfo = ref([])
  const activeUser = ref(null)
  const userData = ref([])
  const productList = ref([])
  const productList2 = ref([])
  const zeroArray = ref(Array(38).fill(0))
  const randomData = ref([])
  const randomData2 = ref([])
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const getRates = function() {
 
    axios({
      method:'get',
      url : 'http://127.0.0.1:8000/exchangerates/get/'
    //   url : 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=uoy62HLCRtJQkYXPFkSABPy5cBNfrzDQ&searchdate=20231116&data=AP01'
    })
    .then(res=>{
      


      ratesResult.value = res.data
      
        
    })
    .catch(err=>{
        // console.log(221)
        console.log(err)
        // console.log(333)

    })
  }
  
  const getFinInfos = async function() {
    const depositProductId = window.location.pathname.split('/').pop();
    try {
      const res = await axios({
        method: 'get',
        url: `http://127.0.0.1:8000/fininfos/deposit-products/${depositProductId}`
      });
     
      finInfosResult.value = res.data;
      productList.value = [];
      finInfosOptions.value = [];
      
      const requests = finInfosResult.value.map(finInfo => {
        return axios({
          method: 'get',
          url: `http://127.0.0.1:8000/fininfos/deposit-products-options/${finInfo.fin_prdt_cd}`,
        });
      });
  
      // 병렬로 모든 API 요청을 수행
      const responses = await Promise.all(requests);
  
      // 각 응답을 finInfosOptions에 추가
      finInfosOptions.value = responses.map(res => res.data);
  
      // productList에 값 추가
      productList.value = finInfosResult.value.map(finInfo => finInfo.fin_prdt_cd);
     
    } catch (err) {
      console.error(err);
    }
  }

  const getFinSavingInfos = async function() {
    const savingProductId = window.location.pathname.split('/').pop();
    
    try {
      const res = await axios({
        method: 'get',
        url: `http://127.0.0.1:8000/fininfos/deposit-products/saving_products/${savingProductId}`
      });
     
      finSavingInfosResult.value = res.data;
      productList2.value=[]
      finSavingInfosOptions.value=[]

      const requests = finSavingInfosResult.value.map(finInfo => {
        return axios({
          method: 'get',
          // url: `http://127.0.0.1:8000/fininfos/deposit-products-options/${finInfo.fin_prdt_cd}`,
          url: `http://127.0.0.1:8000/fininfos/deposit-products-options/saving_products/${finInfo.fin_prdt_cd}`,
        });
      });
  
      // 병렬로 모든 API 요청을 수행
      const responses = await Promise.all(requests);
  
      // 각 응답을 finInfosOptions에 추가
      finSavingInfosOptions.value = responses.map(res => res.data);
  
      // productList에 값 추가
      productList2.value = finSavingInfosResult.value.map(finInfo => finInfo.fin_prdt_cd);
      
    } catch (err) {
      console.error(err);
    }
  };

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/login/',
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log(res.data)
        token.value = res.data.key
        activeUser.value = username
        console.log(activeUser.value)
        console.log(token)
        router.push({ name: 'home' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const { realname, username, password1, password2, age, telphone, money, salary, email } = payload

    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/signup/',
      data: {
        realname, username, password1, password2, age, money, salary, telphone, email
      }
    })
      .then((res) => {
        console.log(res)
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
        window.alert("아이디 혹은 비밀번호가 틀렸습니다.")
      })
  }
  
  const logOut = function () {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/logout/',
    })
      .then((res) => {
        token.value = null
        window.alert("로그아웃되었습니다. 홈으로 이동합니다.")
        router.push({ name: 'home' })
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      headers: {
        Authorization: `Token ${token.value}`
        // Authorization:'Token 438d98c9e0128f4220679fb5d7eb57de8921cfe6'
      }
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log('no article')
        console.log(err)
      })
  }
  
  const getUserInfo = function () {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/user/`,
      data: {
        username: activeUser.value
      },
      headers: {
        Authorization: `Token ${token.value}`
        // Authorization:'Token 438d98c9e0128f4220679fb5d7eb57de8921cfe6'
      }
    })
      .then((res) =>{
        console.log(res.data.pk)
        userId.value = res.data.pk
        console.log(userId.value)
      })
      .catch((err) => {
        console.log('no user')
        console.log(err)
      })
  }


  const getProfile = function () {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/profile/profile/${activeUser.value}`,
      headers: {
        Authorization: `Token ${token.value}`
        // Authorization:'Token 438d98c9e0128f4220679fb5d7eb57de8921cfe6'
      }
    })
      .then((res) =>{
        // console.log(res)
        userInfo.value = res.data
      })
      .catch((err) => {
        console.log('no user')
        console.log(err)
      })
  }
  const getRandom = function() {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/fininfos/recommend/`,
      
    })
      .then((res) =>{
        // console.log(res)
        randomData.value = res.data
      })
      .catch((err) => {
        console.log('no random')
        console.log(err)
      })
  }
  const getRandom2 = function() {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/fininfos/recommend2/`,
      
    })
      .then((res) =>{
        // console.log(res)
        randomData2.value = res.data
      })
      .catch((err) => {
        console.log('no random')
        console.log(err)
      })
  }
  const getUserData = function() {
    axios({
      meghod: 'get',
      url: `http://localhost:8000/profile/recommend/`,
    })
    .then((res)=>{
      userData.value = res.data
      zeroArray.value =Array(38).fill(0)
      // console.log(`getUserData ${zeroArray.value}`)
      // console.log(`fields보자 ${userData.value[0]}`)
      // console.log(`fields보자 ${userData.value[0].fields}`)
      // console.log(zeroArray.value,1111111111111)
      // console.log(`몇번: ${userData.value[0].fields.financial_products}`)
      for (let i=0;i<userData.value.length;i++){
        // console.log(`전체 : ${userData.value[i].fields.financial_products}`)
        let product = userData.value[i].fields.financial_products.split(',')
        for (let j=0;j<userData.value[i].fields.financial_products.length;j++){
          // console.log(`코드 ${product[j]}`)
          for (let k=0;k<38;k++){
            // console.log(`프리 ${productList.value[k]}`)
            if(product[j]===productList.value[k])
              // console.log(`일치, ${k}`)
              zeroArray.value[k]+=1
              

          }
        }
        

      }
      console.log(zeroArray.value,3333333333)
    
      // }
      // console.log(productList.value)

      // console.log(productList.value)
    })
    .catch((err)=>{
      console.log(err)
    })
    
  }

   // DRF에 article 조회 요청을 보내는 action
   const getComments = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/comments',
    })
      .then((res) =>{
        comments.value = res.data
        console.log(comments.value)
      })
      .catch((err) => {
        console.log('no comments')
        console.log(err)
      })
  }

  return { articles,token,getRates,ratesResult,getFinInfos,finInfosResult,finSavingInfosResult,getFinSavingInfos,logIn,signUp,isLogin,getArticles,logOut,getProfile,userInfo,activeUser,getUserData,userData,productList,zeroArray,finInfosOptions
  ,getRandom,randomData,getRandom2,randomData2,getUserInfo,userId,getComments,comments }
}, { persist: true })
