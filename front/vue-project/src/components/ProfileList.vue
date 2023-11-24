<!-- <template>
  <div>
  <div>
    <div class="input-form-backgroud row">
      <div class="input-form col-md-12 mx-auto">
        <form @submit.prevent="signUp">
            <div class="mb-3">
              <label>아이디</label>
              <div>{{ username }}</div>
              </div>
              <div class="mb-3">
              <label for="originpw">기존 비밀번호</label>
            <input class="form-control" id="originpw" type="password" v-model.trim="originpw">
            </div>
            <div class="mb-3">
              <label for="password1">비밀번호 변경</label>
            <input class="form-control" id="password1" type="password" v-model.trim="password1">
            </div>
            <div class="mb-3">
            <label for="password2">비밀번호 변경 확인</label>
            <input class="form-control" id="password2" type="password" v-model.trim="password2">
          </div>
          <div class="mb-3">
          <label>이름</label>
            <p>{{ realname }}</p>
            <hr>
          </div>
            <div class="mb-3">
            <label>나이</label>
            <div>{{ age }}</div>
            <hr>
            </div>
            <div class="mb-3">
            <label for="telphone">전화번호</label>
            <input class="form-control" id="telphone" placeholder="000-0000-0000" v-model.trim="telphone">
            </div>
            <div class="mb-4">
            <label for="email">이메일</label>
            <input class="form-control" id="email" type="text" placeholder="you@example.com" v-model.trim="email">
            </div>
            <hr class="mb-4">
            <button @click="changePassword()" class="signup-btn btn btn-primary btn-lg btn-block col-md-12 mb-2"  type="submit">수정하기</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRateStore } from '@/stores/rate'
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const store = useRateStore()
const router = useRouter()

const userInfo = store.userInfo
const realname = userInfo.realname
const username = userInfo.username
const originpw = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const age = userInfo.age
const telphone = userInfo.telphone
const email = userInfo.email


const changePassword = function () {
axios({
  method: 'post',
  url: 'http://127.0.0.1:8000/accounts/password/change/',
  data: {
    old_password: originpw.value,
    new_password1: password1.value,
    new_password2: password2.value,
  },
  headers: {
    Authorization: `Token ${store.token}`
  }
})
  .then((res) => {
    console.log(res)
    window.alert("개인 정보가 수정되었습니다.")
    router.push({ name: 'ArticleView' })
  })
  .catch((err) => {
    console.log(err)
    console.log(`${store.token}`)
    console.log(userInfo)
    console.log(password1.value)
    console.log(password2.value)
  })
}
</script>

<style scoped>
.input-form {
      max-width: 680px;
      margin-top: 80px;
      padding: 32px;
      background: #ffffff;
      -webkit-border-radius: 10px;
      -moz-border-radius: 10px;
      border-radius: 10px;
      -webkit-box-shadow: 0 8px 20px 0 rgba(0, 0, 0, 0.15);
      -moz-box-shadow: 0 8px 20px 0 rgba(0, 0, 0, 0.15);
      box-shadow: 0 8px 20px 0 rgba(0, 0, 0, 0.15)
    }
.signup-btn {
  --bs-btn-bg: #4f9bd8;
  --bs-btn-border-color: #4f9bd8;
}
</style> -->

<template>
  <div class="container">
    <div class="link">
      <h3>유저 프로필</h3>
    </div>
    <hr>
    <div class="container mt-5">
    <div class="row">
        <div class="col-md-2">
            <!-- 세로 선택바 -->
            <ul class="nav flex-column">
                <li class="nav-item">
                    <a class="nav-link active" href="#">유저 정보</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">차트</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">상품 추천받기</a>
                </li>
            </ul>
        </div>
        <div class="col-md-10">
            <!-- 유저 정보 -->
            <div class="card">
                <div class="card-header d-flex justify-content-between align-items-center" style="min-height: 50px;">
                    <span>유저 정보</span>
                    <button v-if="!isEditMode" class="btn btn-sm btn-primary" @click="editStart">수정하기</button>
                </div>
                <div class="card-body">
                    <!-- 값 표시 -->
                    <table class="table table-borderless">
                        <tbody>
                            <tr>
                                <td class="col-md-2 border-right">
                                    <strong>ID</strong>
                                </td>
                                <td class="col-md-8">
                                    <span>{{ store.userInfo.username }}</span>
                                </td>
                            </tr>
                            <tr>
                                <td class="col-md-2 border-right">
                                    <strong>이름</strong>
                                </td>
                                <td class="col-md-8">
                                  <span>{{ store.userInfo.realname }}</span>
                                </td>
                            </tr>
                            <tr>
                                <td class="col-md-2 border-right">
                                    <strong>Email</strong>
                                </td>
                                <td class="col-md-8">
                                  <span v-if="!isEditMode">{{ store.userInfo.email }}</span>
                                  <input v-else v-model="editInfo.email" type="text"  class="border-input">
                                </td>
                            </tr>
                            <tr>
                                <td class="col-md-2 border-right">
                                    <strong>나이</strong>
                                </td>
                                <td class="col-md-8">
                                  <span v-if="!isEditMode">{{ store.userInfo.age }}</span>
                                  <input v-else v-model="editInfo.age" type="number"  class="border-input">
                                </td>
                            </tr>
                            <tr>
                                <td class="col-md-2 border-right">
                                    <strong>현재 가진 금액</strong>
                                </td>
                                <td class="col-md-8">
                                  <span v-if="!isEditMode">{{ store.userInfo.money }}</span>
                                  <input v-else v-model="editInfo.money" type="number"  class="border-input"> 
                                </td>
                            </tr>
                            <tr>
                                <td class="col-md-2 border-right">
                                    <strong>연봉</strong>
                                </td>
                                <td class="col-md-8">
                                  <span v-if="!isEditMode">{{ store.userInfo.salary }}</span>
                                  <input v-else v-model="editInfo.salary" type="number"  class="border-input"> 
                                </td>
                            </tr>
                            
                        </tbody>
                    </table>
                </div>
                <!-- edit mode에서만 나타남 -->
                <div v-if="isEditMode" class="card-footer">
                  <button class="btn btn-sm btn-success float-right" @click="editComplete">수정 완료</button>
                </div>
            </div>
        </div>
    </div>
    </div>

  </div>
</template>


<script setup>
import { onMounted, ref } from 'vue'
import { useRateStore } from '@/stores/rate'
import axios from 'axios';

const store = useRateStore()
const isEditMode = ref(false)
const editInfo = ref({})


const editStart = () => {
  editInfo.value = store.userInfo
  isEditMode.value = true
}


const editComplete = () => {
  isEditMode.value = false
  axios({
    method: 'put',
    url: 'http://127.0.0.1:8000/accounts/user/',
    headers: {
        Authorization: `Token ${store.token}`
    },
    data: editInfo.value
  })
  .then(res => {
    console.log(res)
    store.getUserInfo()
  })
  .catch(err => console.log(err))
}

</script>


<style scoped>
input::-webkit-inner-spin-button {
  appearance: none;
  -moz-appearance: none;
  -webkit-appearance: none;
}
.container {
  padding-top: 20px;
  padding-bottom: 20px;
}

.bread-crumb > a {
  text-decoration: none;
  color: black;
  font-size: small;
}

.border-right {
  border-right: 1px solid #dee2e6;
}

/* .border-input {
  border: 0.5px solid #ccc;
} */

</style>