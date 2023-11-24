<template>
  <div class="community">
    <div class="community-inner">
      <div class="input-form-backgroud row">
          <div class="input-form col-md-9 mx-auto">
            <h2 class="mb-5 text-center fw-semibold">게시글 수정</h2>
      <form @submit.prevent="updateArticle">
        <div class="mb-4">
          <label class="fs-5" for="title">제목</label>
          <input class="form-control form-control-lg col-md-6" type="text" v-model.trim="title" id="title">
        </div>
        <div class="mb-4">
          <label class="fs-5" for="content">내용</label>
          <textarea class="form-control" style="height: 300px" v-model.trim="content" id="content"></textarea>
        </div>
        <button class="create-btn btn btn-primary btn-md btn-block mb-2"  type="submit">수정</button>
      </form>
    </div>
  </div>
</div>
</div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  import { useRateStore } from '@/stores/rate'
  import { useRouter, useRoute } from 'vue-router'
  
  const store = useRateStore()
  const router = useRouter()
  const route = useRoute()

  const article = ref(null)
  const title = ref(null)
  const content = ref(null)

onMounted(() => {
  
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/articles/${route.params.id}/`
  })
    .then((res) => {
      // console.log(res.data)
      article.value = res.data
      title.value = article.value.title
      content.value = article.value.content

    })
    .catch((err) => {
      console.log(err)
    })
})

  const updateArticle = function () {
  axios({
    method: 'put',
    url: `http://127.0.0.1:8000/api/v1/articles/${route.params.id}/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      // console.log(res)
      router.push({ name: 'ArticleView' })
    })
    .catch((err) => {
      console.log(err)
    })
}
  
  
  </script>
  
  <style scoped>
  .create-btn {
    /* background-color: #ff9b21;
    background-color: #4f9bd8; */
    --bs-btn-bg: #4f9bd8;
    --bs-btn-border-color: #4f9bd8;
  }
  </style>
  