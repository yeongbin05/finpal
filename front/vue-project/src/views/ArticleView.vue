<template>
  <div class="community">
    <div class="community-inner">
    <h1 class="mb-4 mt-5 text-center fw-semibold">게시판</h1>
    <div class="regist-area">
      <RouterLink :to="{ name: 'ArticleCreateView' }">
        <button type="button" class="btn btn-primary create-btn">글 작성</button>
      </RouterLink>
    </div>
    <ArticleList />
  </div>
</div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRateStore } from '@/stores/rate'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useRateStore()

onMounted(() => {
  store.getArticles()
})

</script>

<style scoped>

.create-btn {
  margin-right: 60px; /* Adjust the left margin as needed */
}
.regist-area {
    padding: 8px;
    text-align: right;
}

.table th {
  width: auto; /* Adjusted to allow natural width */
}

/* .regist-btn { */
  /* background-color: #ff9b21;
  background-color: #4f9bd8; */
  /* --bs-btn-bg: #4f9bd8;
  --bs-btn-border-color: #4f9bd8; */
/* } */

.community {
  display: flex;
  justify-content: center;
}

.community-inner {
  border-radius: 10px;
  background-color: white;
  width: 90%;
  height: 680px;
  margin-top: 100px;
  margin-bottom: 100px;
  text-align: center;
}
</style>
