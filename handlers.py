from aiogram import Router, types
from aiogram.filters import CommandStart

# Создаём роутер (маршрутизатор) для обработки команд
router = Router()

# Обработчик команды /start
@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("""Привет!
Мы команда профессионалов, создаём песни для героев, превращая их истории в музыку.

Вы можете подарить песню близкому на фронте или, находясь на передовой, передать его родным. Музыка навсегда увековечит историю и имя героя. 

Жми на старт – и мы создадим для вас песню""")
