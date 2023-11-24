<template>
  <!-- <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <RouterLink :to="{ name: 'ArticleDetailView', params: { id: article.id }}">
      [Detail]
    </RouterLink>
    <hr>
  </div> -->
  <div class="container">
    <div class="board-list">
    
      <table class="table table-hover">
      <!-- <thead>
      <tr>
        <th>No</th>
        <th>제목</th>
        <th>등록일시</th>
      </tr>
      </thead> -->
      <tbody>
      <tr>
        <td>{{ article.id }}</td>
        <td><a v-on:click="">{{ article.title }}</a></td>
        <td>{{ article.created_at }}</td>
        <td><RouterLink :to="{ name: 'ArticleDetailView', params: { id: article.id }}">
        [Detail]
        </RouterLink></td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>

<style scoped>
.board-list {
    width: 768px;
    margin: auto;
}

.board-detail {
    width: 768px;
    margin: auto;
    text-align: left;
}

.board-contents {
    padding: 12px 8px;
    border-bottom: 1px solid #eee;
}
</style>
