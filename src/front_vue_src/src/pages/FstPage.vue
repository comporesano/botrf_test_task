<script setup lang="ts">
import { ref } from 'vue';
import { useWebApp } from 'vue-tg';
import { useUserManagerStore } from '@/store/useUserManager';
import { DateTimePicker } from 'vue-drumroll-datetime-picker'
import { useRouter } from 'vue-router';

import 'vue-drumroll-datetime-picker/dist/style.css'
import '../index.css'

interface User {
    birth_date: string;
    first_name: string;
    last_name: string;
    username: string;
}
// const { initData } = useWebApp();
// const userData = JSON.parse(initData);
const birthDate = ref('');
const store = useUserManagerStore();
const router = useRouter();

async function handleSubmit() {
    console.log(birthDate.value)
    try {
      await fetch('http://0.0.0.0:8080/user/create', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          first_name: '',
          last_name: '',
          username: '',
          birth_date: birthDate.value
        })
      });
      store.setCurrentUser({
        first_name: '',
        last_name: '',
        username: '',
        birth_date: birthDate.value
      });
      router.push('/second-page');
    } catch (error) {
      console.error(error)
    }
    
    console.log(store.currentUser);
}
</script>

<template>
    <div class="body bg-corn min-h-screen flex justify-center items-center">
        <div class="text-one-style flex justify-center items-center flex-col">
            <h1 class="title text-lg underline">Выберите свою дату рождения:</h1>
            <DateTimePicker v-model='birthDate' class="text-3xl" type="date"/>
            <button @click="handleSubmit" class="flex justify-center items-center rounded-md btn-submit text-xl">Подтвердить</button>
        </div>
    </div>
</template>

<style lang="css">
.v-drumroll-picker {
    --selected-color: white
}
.vue-scroll-picker-item-selected {
    color: black;
}
.btn-submit {
    border-width: 1px;
    border-color: black;
    padding-top: 3px;
}
.bg-corn {
    background-color: white;
}
.text-one-style {
    font-family: 'Courier New', Courier, monospace;
}
</style>

