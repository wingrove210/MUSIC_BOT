import asyncio
from aiogram import Bot, Dispatcher
from handlers import router  
from config import settings

# Укажите свой токен
TOKEN = settings.BOT_TOKEN

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Регистрируем хендлеры
    dp.include_router(router)

    # Запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    # if settings.ENVIRONMENT == "local":
    #     print(settings.BOT_TOKEN)
    # else:
    #     print("It's production")
    asyncio.run(main())
