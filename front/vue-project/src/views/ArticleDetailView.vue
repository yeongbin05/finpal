<template>
  <div class="community">
    <div class="community-inner">
      <div class="input-form-backgroud row">
       <div class="input-form col-md-12 mx-auto">
        <h2 class="mb-5 mt-5 text-center fw-semibold">{{ articleIndex }}번 게시물</h2>
          <div v-if="article">
            <table class="table">
            <tr>
            <th width=10%>번호</th>
            <td>{{ article.id }}</td>
            </tr>
            <tr>
            <th width=10% class="text-center warning">작성일</th>
            <td width=40% class="text-center warning">{{ article.created_at.split("T")[0] }}</td>
            <th width=10% class="text-center warning">수정일</th>
            <td width=40% class="text-center warning">{{ article.updated_at.split("T")[0] }}</td>
            </tr>
            <tr>
            <th>제목</th>
            <td>{{ article.title }}</td>
            </tr>
            <tr>
            <th>내용</th>
            <td>{{ article.content }}</td>
            <!-- <td>{{ article }}</td> -->
            </tr>
            <tr>
            <td colspan="4" class="text-right">
              <div v-if="isSameUser">
                <button @click="goUpdate" type="button" class="btn btn-xs btn-info">수정</button>
                <button @click="deleteArticle(article.id)" class="btn btn-xs btn-warning">삭제</button>
                <button @click="goList" class="btn btn-xs btn-success">목록</button>
              </div>

              <div v-else>
                <button @click="goList" class="btn btn-xs btn-success">목록</button>
              </div>

            </td>
            </tr>
            </table>
          </div>
          <hr>
          <div>
            <CommentView 
            :comments = "comments"
            />
          </div>
        </div>
      </div>
    </div>
  </div>




</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRateStore } from '@/stores/rate'
import { useRoute } from 'vue-router'
import router from '../router';
import { computed } from '@vue/reactivity';
import CommentView from '@/views/CommentView.vue';

const store = useRateStore()
const route = useRoute()
const article = ref(null)
const articleIndex = ref(`${route.params.id}`)
const comments = ref([])
onMounted(() => {
axios({
  method: 'get',
  url: `http://127.0.0.1:8000/api/v1/articles/${route.params.id}/`
})
  .then((res) => {
    console.log(res.data)
    console.log(123)
    article.value = res.data
    comments.value = res.data.comment_set
    console.log(comments.value)
  })
  .catch((err) => {
    console.log(err)
  })

store.getComments()
})

const title = ref(null)
const content = ref(null)

const goUpdate = function () {
router.push({ name: 'ArticleUpdateView' })
}

const goList = function () {
router.push({ name: 'ArticleView' })
}

const isSameUser = computed(() => {
console.log(store.userId)
console.log(article.value.user)
if ( article.value.user === store.userId) {
  return true
} else {
  return false
}
})

const deleteArticle = function (articleId) {
  axios({
    method: 'delete',
    url: `http://127.0.0.1:8000/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
      // Authorization:'Token 438d98c9e0128f4220679fb5d7eb57de8921cfe6'
    }
  })
    .then((res) =>{
      console.log(res)
      router.push({ name: 'ArticleView' })
    })
    .catch((err) => {
      console.log('실패')
      console.log(err)
    })
}



</script>

<style scoped>.community {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.community-inner {
  border-radius: 10px;
  background-color: white;
  width: 95%;
  padding: 20px;
}

.article-details {
  max-width: 800px; /* Adjusted max-width for better readability */
  margin: 0 auto; /* Center the article details */
}

.article-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px; /* Adjusted margin for better spacing */
}

.article-table th, .article-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.article-table th {
  background-color: #f2f2f2;
}

.article-title {
  text-align: center;
  margin-bottom: 20px; /* Adjusted margin for better spacing */
}

.text-right {
  text-align: right;
}

.btn {
  margin-right: 10px; /* Adjusted margin for button spacing */
}
</style>
