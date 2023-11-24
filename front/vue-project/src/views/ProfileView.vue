<template>
    <div class="whole">
        <h1>{{ store.activeUser }}님의 프로필</h1>
        <div>
            <h2>기본 정보 수정</h2>
            
        </div>
        <div class="custom-flex">
            <div >
                <a href="/profile"><h2>프로필 수정</h2></a>
                <a href="/cart"><h2>가입 상품</h2></a>
            </div>
            <div class="right-profile">
            <ProfileList />
        </div>
    </div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRateStore } from '@/stores/rate'
import ProfileList from '@/components/ProfileList.vue'

const store = useRateStore()


onMounted(() => {
  store.getProfile()
})


</script>

<style scoped>
.whole {
    padding : 20px;
}
.custom-flex {
    display : flex;
    justify-content: center;
    align-items: center;
}
.custom-flex > div {
    margin-right: 50px;
    margin-bottom : 40px;
}
h2,h1 {
    color : white;
}

.right-profile {
    width : 50%;
}
</style>