<template>
    <form @submit.prevent="handleSubmit">
      <h1>Lox</h1>
    </form>
  </template>
  
  <script setup lang="ts">
  import { ref } from 'vue';
  import { useWebApp } from 'vue-tg';
  import { useUserManagerStore } from '@/store/useUserManager';
  
  const birthDate = ref('');
  const { initData } = useWebApp();
  const userData = JSON.parse(initData);
  const store = useUserManagerStore();
  
  console.log(userData.first_name);
  console.log(userData.last_name);
  
  async function handleSubmit() {
    try {
      await fetch('http://localhost:8080/user/create', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          first_name: userData.first_name,
          last_name: userData.last_name,
          username: userData.username,
          birth_date: birthDate.value
        })
      });
      store.setCurrentUser({
        first_name: userData.first_name,
        last_name: userData.last_name,
        username: userData.username,
        birth_date: birthDate.value
      });
    } catch (error) {
      console.error(error)
    }
  }
  </script>
  