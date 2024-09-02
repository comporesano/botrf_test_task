<script setup lang="ts">
        import { ref } from 'vue';
        import { useUserManagerStore } from '@/store/useUserManager';
        import { DateTimePicker } from 'vue-drumroll-datetime-picker'
        import { initInitData, initUtils } from '@telegram-apps/sdk'

        import 'vue-drumroll-datetime-picker/dist/style.css'
        import '../index.css'

        const birthDate = ref('');
        const store = useUserManagerStore();

        const profile_show = ref(false);
        const tg_data = initInitData();
        const tg_utils = initUtils();

        const data = {
                first_name: tg_data?.user?.firstName ?? '',
                last_name: tg_data?.user?.lastName ?? '',
                username: tg_data?.user?.username ?? '',
                birth_date: birthDate.value
            }
        const api_response = ref({ 
                first_name: '',
                last_name: '',
                username: '',
                day_until_birthday: 0
            })
            
        const initial_data = String(tg_data?.startParam).split('_') ?? [];
        if (initial_data.length > 1) {
            if (Boolean(initial_data[0])) {
                profile_show.value = true;
                const data = getUserInfo(initial_data[1]);
            }
        }
        else {
            const data = {
                first_name: tg_data?.user?.firstName ?? '',
                last_name: tg_data?.user?.lastName ?? '',
                username: tg_data?.user?.username ?? '',
                birth_date: birthDate.value
            }
            profile_show.value = false;
            store.setCurrentUser(data);
        }
        const url = ref(`https://t.me/test_task_botrf_bot/testapp/?startapp=true_${tg_data?.user?.username}`);

        async function getUserInfo(username: string): Promise<{
            first_name: string;
            last_name: string;
            username: string;
            day_until_birthday: number; }> {
                const response = await fetch('https://052992bb089d0c.lhr.life/user/get/?username=' + username, {
                    method: 'GET',
                    headers: {'Content-Type': 'application/json'}
                });
            api_response.value = await response.json()    
            return await response.json();
        }

        async function handleSubmit() {
            try {
            await fetch('https://052992bb089d0c.lhr.life/user/create', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    first_name: tg_data?.user?.firstName ?? '',
                    last_name: tg_data?.user?.lastName ?? '',
                    username: tg_data?.user?.username ?? '',
                    birth_date: birthDate.value
                })
            });
            profile_show.value = true;          
            } catch (error) {
            console.error(error)
            }
            api_response.value = await getUserInfo(store.currentUser.username);
        }

        
        async function openLink() {
            await tg_utils.openTelegramLink(
                `https://t.me/share/url?url=${url.value}&text="Моя карточка:3 "`
            );
        }
    </script>
    <template>
        <div v-if="profile_show === false" class="body bg-corn min-h-screen flex justify-center items-center">
            <div class="text-one-style flex justi   fy-center items-center flex-col">
                <h1 class="title text-lg underline">Выберите свою дату рождения:</h1>
                <DateTimePicker v-model='birthDate' :max-date="new Date().toISOString().split('T')[0]" class="text-3xl mt-10" type="date"/>
                <button @click="handleSubmit" class="flex justify-center items-center rounded-md btn-submit mt-10 text-xl">Подтвердить</button>
            </div>
        </div>
        <div v-if="profile_show === true" class="body bg-corn min-h-screen flex justify-center items-center">
        <div class="text-one-style flex justify-center items-center flex-col">
            <h1 class="underline sm:text-3xl">Ваши данные</h1>
            <div class="flex justify-center flex-row sm:text-xl text-sm">
                <ul class="space-y-10">
                    <li class="mt-10">Ваше имя: </li>
                    <li>Ваша фамилия: </li>
                    <li>Ваш телеграм никнейм: </li>
                    <li>Дней до вашего дня рождения: </li>
                </ul>
                <ul class="space-y-10 sm:ml-10 ml-3">
                    <li class="mt-10">{{ data.first_name }}</li>
                    <li>{{ data.last_name }}</li>
                    <li>{{ data.username }}</li>
                    <li>{{ api_response.day_until_birthday }}</li>
                </ul>
            </div>
            <button @click="openLink" class="flex mt-5 justify-center items-center rounded-md btn-submit sm:text-xl text-sm">Поделиться</button>
        </div>
    </div>
    </template>

    <style lang="css">
    .v-drumroll-picker {
        --selected-color: white
    }
    .vue-scroll-picker-layer-top {
        background: none;
    }
    .vue-scroll-picker-layer-bottom {
        background: none;
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


