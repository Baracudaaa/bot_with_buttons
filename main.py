from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove
)

BOT_TOKEN = '8378863385:AAHvtk49agddT8V5u8utvzhHm3zn-heA3MU'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
kb_builter = ReplyKeyboardBuilder()

# Создаем объекты кнопок
button_1 = KeyboardButton(text='Собак 🦮')
button_2 = KeyboardButton(text='Огурцов 🥒')
buttons = [KeyboardButton(text=f'Кнопка {i + 1}') for i in range(10)]
# Создаем объект клавиатуры, добавляя в него кнопки
keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]],
                               resize_keyboard=True,
                               one_time_keyboard=True)
kb_builter.row(*buttons, width=4)
# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Чего больше боятся кошки?',
        reply_markup=kb_builter.as_markup(resize_keyboard=True)
    )

# Этот хэндлер будет срабатывать на ответ "Собак" и удалять клавиатуру
@dp.message(F.text == 'Собак 🦮')
async def process_dog_answer(message: Message):
    await message.answer(
        text='Да, несомненно, кошки боятся собак. '
             'Но вы видели как они боятся огурцов?',
        #reply_markup=ReplyKeyboardRemove()
    )

# Этот хэндлер будет срабатывать на ответ "Огурцов" и удалять клавиатуру
@dp.message(F.text == 'Огурцов 🥒')
async def process_cucumber_answer(message: Message):
    await message.answer(
        text='Да, иногда кажется, что огурцов '
             'кошки боятся больше',
        #reply_markup=ReplyKeyboardRemove()
    )


if __name__ == '__main__':
    dp.run_polling(bot)