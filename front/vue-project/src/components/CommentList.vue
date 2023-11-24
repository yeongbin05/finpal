<template>
  <div>
    <p>{{ comment.content }}-{{ comment.content }}</p>
    <button @click="openUpdateModal()" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal">수정</button> /
    <button @click="deleteComment(comment.id)" class="btn btn-xs btn-warning">삭제</button>
  </div>

   <!-- 수정 모달 창 -->
   <div v-if="isUpdateModalOpen" class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">댓글수정</h5>
            <button @click="closeUpdateModal" type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <textarea v-model="updatedComment" class="form-control"></textarea>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-outline-secondary" @click="closeUpdateModal" data-bs-dismiss="modal">삭제</button>
            <button type="button" class="btn btn-outline-primary" @click="saveUpdatedComment(comment.id)">수정</button>
          </div>
        </div>
      </div>
    </div>

</template>

<script setup>
import { useRateStore } from '@/stores/rate'
import { useRouter, useRoute } from 'vue-router'
import { ref, computed } from 'vue';
import axios from 'axios'

const store = useRateStore()
const router = useRouter()
const route = useRoute()

const isCommentList = computed(() => {
  if ( store.comments) {
    return true
  } {
    return false
  }
})
const props = defineProps({
  comment : Object
})
const deleteComment = function (commentId) {
    axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/api/v1/comments/${commentId}/`,
    })
      .then((res) =>{
        console.log(res)
        // router.push({ name: 'ArticleDetailView', params: { id: route.params.id}})
        location.reload()
      })
      .catch((err) => {
        console.log('실패')
        console.log(err)
      })
  }

// 날짜 포멧
const formatDate = (dateTimeString) => {
  const dateObject = new Date(dateTimeString);
  const options = {
    year: '2-digit',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    hourCycle: 'h23', // Use 24-hour format
  };
  const formattedDate = new Intl.DateTimeFormat('en-US', options).format(dateObject);
  return formattedDate.replace(/,/g, '');}

  // 코멘트 수정
const updatedComment = ref(null);
const isUpdateModalOpen = ref(true);

const openUpdateModal = () => {
  console.log(props.comment)
  updatedComment.value = props.comment.content;
  isUpdateModalOpen.value = true;
  console.log(isUpdateModalOpen.value)
};

const closeUpdateModal = () => {
  isUpdateModalOpen.value = false;
};

const saveUpdatedComment = (commentId) => {
  axios({
    method: 'put',
    url: `http://127.0.0.1:8000/api/v1/comments/${commentId}/`,
    data: {
      content: updatedComment.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log('댓글 수정 완료', res.data);
      closeUpdateModal();
      location.reload()
    })
    .catch((err) => {
      console.error('댓글 수정 실패', err);
    });
};
</script>

<style scoped>
td > a {
    text-decoration: none;
    color: inherit;
}
</style>