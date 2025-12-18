import os
from aiogram.types.web_app_info import WebAppInfo
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (
KeyboardButton,
    KeyboardButtonRequestChat,
    KeyboardButtonRequestUser,
    KeyboardButtonRequestUsers,
    Message,
    ReplyKeyboardMarkup,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

BOT_TOKEN = '8378863385:AAHvtk49agddT8V5u8utvzhHm3zn-heA3MU'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаем кнопки
request_user_btn = KeyboardButton(
    text="Выбрать пользователя",
    request_user=KeyboardButtonRequestUser(
        request_id=42,
        user_is_premium=False
    )
)

request_users_btn = KeyboardButton(
    text='Выбрать пользователей',
    request_users=KeyboardButtonRequestUsers(
        request_id=77,
        user_is_premium=False,
        max_quantity=3
    )
)

request_chat_btn = KeyboardButton(
    text='Выбрать чат',
    request_chat=KeyboardButtonRequestChat(
        request_id=1408,
        chat_is_channel=False,
        chat_is_forum=False
    )
)

web_app_btn = KeyboardButton(
    text='Start Web App',
    web_app=WebAppInfo(url="https://habr.com/ru/articles/817445/?ysclid=mgxslh46q7405871598")
)

# Добавляем кнопки в билдер
kb_builder.row(request_chat_btn, request_user_btn, request_users_btn, web_app_btn, width=1,)

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
)
keyboard.input_field_placeholder = 'Рады вас приветствовать!'
# /start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text="Экспериментируем со специальными кнопками",
        reply_markup=keyboard
    )

@dp.message(Command(commands='web_app'))
async def process_web_app_command(message: Message):
    await message.answer(
        text='Экспериментируем со специальными кнопками',
        reply_markup=keyboard
    )

# Этот хэнлер будет срабатывать на выбор пользователей из списка
@dp.message(F.user_shared)
async def process_user_shared(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))


# Этот хэндлер будет срабатывать на выбор пользователей из списка
@dp.message(F.users_shared)
async def process_users_shared(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))


# Этот хэндлер будет срабатывать на выбор чата из списка
@dp.message(F.chat_shared)
async def process_chat_shared(message: Message):
    print(message.model_dump_json(indent=4, exclude_none=True))


if __name__ == '__main__':
    dp.run_polling(bot)