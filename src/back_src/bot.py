from aiogram import Bot, Dispatcher, types, enums
from aiogram.filters import Command
from aiogram.dispatcher.router import Router

from bot_config import TOKEN

import asyncio


class UserManagerBot(Bot):
    """Classic user manager bot and tg mini app provider"""
    
    def __init__(self, token: str) -> None:
        super().__init__(token=token)
        

umbot = UserManagerBot(token=TOKEN)
dp = Dispatcher()
router = Router()

"""Bot routing"""
@router.message(Command('start'))
async def start_message(msg: types.Message) -> None:
    #params = f'?first_name={msg.from_user.first_name}&last_name={msg.from_user.last_name}&username={msg.from_user.username}'
    params = ''
    await msg.answer(text=f'<b>Hello there, {msg.from_user.first_name}!</b>',
                     reply_markup=types.InlineKeyboardMarkup(
                         inline_keyboard=[
                             [types.InlineKeyboardButton(text='To APP', url=f'https://t.me/test_task_botrf_bot/testapp{params}')]
                         ]),
                     parse_mode=enums.ParseMode.HTML)
"""Bot routing"""


async def main() -> None:
    dp.include_router(router=router)
    await dp.start_polling(umbot, allowed_updates=dp.resolve_used_update_types())
    

if __name__ == "__main__":
    asyncio.run(main=main())
    