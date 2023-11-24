<template>
  <p>댓글</p>
  <div v-if="isComments">
      <CommentList v-for="comment in comments"
      :comment = "comment"/>
  </div>
 
  <div v-else>
       <p style="color: orange;">아직 작성된 댓글이 없습니다. 댓글을 달아주세요.</p>
  </div>
 
 <form @submit.prevent="createComment" class="comment-form">
     <div class="mb-4 d-flex align-items-center">
     <input class="form-control form-control-lg" type="text" v-model.trim="content" placeholder="댓글을 입력해주세요." id="content">
     <button class="create-btn btn btn-primary btn-md ml-2"  type="submit">등록</button>
     </div>
 </form>
 </template>
 
 <script setup>
 import CommentList from '@/components/CommentList.vue';
 import { ref, computed } from 'vue'
 import axios from 'axios'
 import { useRateStore } from '@/stores/rate'
 import { useRoute, useRouter } from 'vue-router'
 
 const store = useRateStore()
 const route = useRoute()
 const router = useRouter()
 
 const content = ref(null)
 const props = defineProps({
   comments : Array
 })
 const comments = computed(() => {
   return props.comments
 })
 
 const isComments = computed(() => {
   console.log(comments.value)
   if ( comments.value.length === 0 ) {
     return false
   } else {
     return true
   }
 })
 
 const createComment = function () {
   axios({
     method: 'post',
     url: `http://127.0.0.1:8000/api/v1/articles/${route.params.id}/comments/`,
     data: {
       content: content.value
     },
     headers: {
       Authorization: `Token ${store.token}`
       // Authorization: 'Token 438d98c9e0128f4220679fb5d7eb57de8921cfe6'
     }
   })
     .then((res) => {
       console.log(res)
       // router.push({ name: 'ex2' })
       console.log(route.params.id)
       // router.push({ name: 'ArticleDetailView', params: {id: route.params.id } })
       // router.push({ name: 'ex2'})
       location.reload()
       // router.push({ name: 'ArticleDetailView', params: {id: route.params.id} })
     })
     .catch((err) => {
       console.log(err)
     })
   }
 
 </script>
 
 <style scoped>
  .comment-form {
  width: 100%;
  }

  .create-btn {
    flex: 0 0 auto;
  }
 </style>