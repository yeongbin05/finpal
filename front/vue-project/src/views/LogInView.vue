<template>
  <div>
    <div>
      <div class="input-form-backgroud row">
        <div class="input-form col-md-9 mx-auto">
          <h2 class="mb-4 text-center fw-semibold">로그인</h2>
          <form @submit.prevent="logIn">
            <div>
            <label for="username"></label>
            <input class="form-control form-control-lg col-md-6" id="username" placeholder="아이디" type="text" v-model.trim="username">
            </div>
            <div class="mb-4">
            <label for="password"></label>
            <input class="form-control form-control-lg" id="password" placeholder="비밀번호" type="password" v-model.trim="password">
            </div>
            <button class="login-btn btn btn-primary btn-lg btn-block col-md-12 mb-2"  type="submit">로그인</button>
            <!-- <button class="btn btn-primary btn-lg btn-block col-md-12" type="submit">회원가입</button> -->
            </form>
          </div>
        </div>
      </div>
    </div>


</template>

<script setup>
import { ref } from 'vue'
import { useRateStore } from '@/stores/rate'

const store = useRateStore()
const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
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

.login-btn {
  /* background-color: #ff9b21;
  background-color: #4f9bd8; */
  --bs-btn-bg: #4f9bd8;
  --bs-btn-border-color: #4f9bd8;
}
</style>