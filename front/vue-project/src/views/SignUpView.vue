<template>
  <div>
    <!-- <form class="signup-form">
      아이디 : <input type="text">
      비밀번호 : <input type="text">
      이름 : <input type="text">
      생년월일 : <input type="text">
      전화번호 : <input type="text">
      이메일 : <input type="text">
      
      <input type="submit" name="" id="">
    </form> -->
  <div>
    <div class="input-form-backgroud row">
      <div class="input-form col-md-12 mx-auto">
        <h2 class="mb-4 text-center fw-semibold">회원가입</h2>
        <form @submit.prevent="signUp">
          <!-- <label for="iD">아이디:</label>
            <input id="iD" type="text" v-model.trim="iD">
            <br> -->
            <div class="mb-3">
              <label for="username">아이디</label>
              <input class="form-control" id="username" type="text" v-model.trim="username">
              </div>
            <div class="mb-3">
              <label for="password1">비밀번호</label>
            <input class="form-control" id="password1" type="password" v-model.trim="password1">
            </div>
            <div class="mb-3">
            <label for="password2">비밀번호 확인</label>
            <input class="form-control" id="password2" type="password" v-model.trim="password2">
          </div>
          <div v-if="isSame === 1">
            <p style="color: blue;">비밀번호가 일치합니다.</p>
          </div>
          <div v-else-if="isSame === 2">
            <p></p>
          </div>
          <div v-else>
            <p style="color: red;">비밀번호가 일치하지 않습니다.</p>
          </div>
          <div class="mb-3">
          <label for="realname">이름</label>
          <input class="form-control" id="realname" type="text" v-model.trim="realname">
          </div>
            <div class="mb-3">
            <label for="age">나이</label>
            <input class="form-control" id="age" placeholder="만 나이" v-model.trim="age">
            </div>
            <div class="mb-3">
            <label for="telphone">전화번호</label>
            <input class="form-control" id="telphone" placeholder="000-0000-0000" v-model.trim="telphone">
            </div>
            <div class="mb-4">
            <label for="email">이메일</label>
            <input class="form-control" id="email" type="text" placeholder="you@example.com" v-model.trim="email">
            </div>
            <div class="mb-4">
            <label for="money">보유 자산</label>
            <input class="form-control" id="money" type="text" placeholder="예시) 1000000" v-model.trim="money">
            </div>
            <div class="mb-4">
            <label for="salary">월급</label>
            <input class="form-control" id="salary" type="text" placeholder="예시) 1000000" v-model.trim="salary">
            </div>
            <hr class="mb-4">
            <button class="signup-btn btn btn-primary btn-lg btn-block col-md-12 mb-2"  type="submit">가입하기</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRateStore } from '@/stores/rate'

const store = useRateStore()
const realname = ref(null)
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const age = ref(null)
const telphone = ref(null)
const email = ref(null)
const money = ref(null)
const salary = ref(null)

const isSame = computed(() => {
  // 패스워드 둘다 null이 아니고 값이 같을 때
  if ( password1.value != null && password2.value != null && ( password1.value === password2.value)) {
    return 1
  //  패스워드 둘 중 하나가 null일 떄
  } else if ( (password1.value === null || password2.value === null )) {
    return 2
  // 그 외 상황
  } else {
    return 3
  }
});

const signUp = function () {
  const payload = {
    realname: realname.value,
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    age: age.value,
    telphone: telphone.value,
    email: email.value,
    money: money.value,
    salary: salary.value,
  }
  store.signUp(payload)
}


</script>

<style scoped>
/* .signup-form {
  border : 1px solid grey;
  width : 90%;
  margin-left : 30px;
  display  : flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
} */
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
  /* background-color: #ff9b21;
  background-color: #4f9bd8; */
  --bs-btn-bg: #4f9bd8;
  --bs-btn-border-color: #4f9bd8;
}
</style>