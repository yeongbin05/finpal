<template>
  <div class="community">
   <div class="community-inner">
    <div class="input-form-backgroud row">
        <div class="input-form col-md-9 mx-auto">
          <h2 class="mb-5 mt-5 text-center fw-semibold">게시글 작성</h2>
        <div class="create-area">
          <form @submit.prevent="createArticle">
            <div class="mb-4">
              <label class="fs-5" for="title">제목</label>
              <input class="form-control form-control-lg col-md-6" type="text" v-model.trim="title" id="title" maxlength="30">
            </div>
          <div class="mb-4">
              <label class="fs-5" for="content">내용</label>
              <textarea class="form-control" style="height: 300px" v-model.trim="content" id="content" maxlength="200"></textarea>
            </div>
            <button class="create-btn btn btn-primary btn-md btn-block mb-5"  type="submit">등록</button>
            <button @click="goList()" class="list-btn btn btn-secondary btn-md btn-block mb-5 mx-1">목록</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRateStore } from '@/stores/rate'
import { useRouter } from 'vue-router'

const title = ref(null)
const content = ref(null)
const store = useRateStore()
const router = useRouter()

const goList = function () {
  const userConfirmed = window.confirm("게시글 작성을 취소하시겠습니까?");
  if (userConfirmed) {
        router.push({ name: "ArticleView" });
      }
}

const createArticle = function () {
  if ( title.value === null || content.value === null ) {
    window.alert("제목 또는 내용을 입력해주세요.")
  } else {
  axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/api/v1/articles/',
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
      // Authorization: 'Token 438d98c9e0128f4220679fb5d7eb57de8921cfe6'
    }
  })
    .then((res) => {
      // console.log(res)
      router.push({ name: 'ArticleView' })
    })
    .catch((err) => {
      console.log(title.value)
      console.log(content.value)
      console.log(`${store.token}`)
    })
  }
}



</script>

<style scoped>
.create-btn {
  /* background-color: #ff9b21;
  background-color: #4f9bd8; */
  --bs-btn-bg: #4f9bd8;
  --bs-btn-border-color: #4f9bd8;
}
.community {
  display: flex;
  justify-content: center;
}
.community-inner {
  border-radius: 10px;
  background-color: white;
  width: 95%;
  margin-top: 100px;
}

.create-area {
  text-align: left;
}

</style>
