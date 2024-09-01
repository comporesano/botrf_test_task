<template>
    <div class="pages-app">
        <h1>Test</h1>
        <fp-page />
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import FirstPageForm from './FirstPageForm.vue';

export default defineComponent({
    components: { FirstPageForm },
    setup() {
        return {};
    },
})

</script>       