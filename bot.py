import asyncio
from aiogram import Bot, Dispatcher
from handlers import router  # Импортируем маршрутизатор из handlers.py

# Укажите свой токен
TOKEN = "8151650888:AAFSJqYDHUtrii-7WS8sBDgi0MGtmYosg9k"

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Регистрируем хендлеры
    dp.include_router(router)

    # Запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
