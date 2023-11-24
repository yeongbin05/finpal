<template>
  <div>
    <div class="board-list">
      <table class="table table-bordered table-hover">
        <thead>
          <tr>
            <th style="width: 15%;">No</th>
            <th style="width: 40%;">제목</th>
            <th style="width: 30%;">작성자</th>
            <th style="width: 20%;">등록일</th>
          </tr>
        </thead>
        <tbody class="table-group-divider">
          <tr v-for="article in store.articles" :key="article.id" v-if="isArticleList">
            <td>{{ article.id }}</td>
            <td><RouterLink :to="{ name: 'ArticleDetailView', params: { id: article.id }}">
              {{ article.title }}
            </RouterLink></td>
            <td>{{ article.user }}</td>
            <td>{{ article.created_at.split("T")[0] }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script setup>
import { useRateStore } from '@/stores/rate'
import ArticleListItem from '@/components/ArticleListItem.vue'
import { computed } from 'vue';

const store = useRateStore()

const isArticleList = computed(() => {
  if ( store.articles) {
    return true
  } {
    return false
  }
})

console.log(store.articles)
</script>

<style scoped>

.table {
  width: 90%;
  margin: 0 auto;
}

.table-bordered th, .table-bordered td {
  border: 1px solid #dee2e6;
}

.table-bordered thead th, .table-bordered thead td {
  border-bottom-width: 2px;
}

.table-hover tbody tr:hover {
  background-color: #f5f5f5;
}

.table-group-divider tbody tr:last-child {
  border-bottom: 2px solid #dee2e6;
}

.board-list {
  margin-top: 20px;
}

</style>