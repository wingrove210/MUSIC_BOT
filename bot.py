import asyncio
import json
from typing import Union, Dict, Any
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Filter
from config import settings
from aiogram.filters import CommandStart
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTION"],
    allow_headers=["*"]
)

# Укажите свой токен
TOKEN = settings.BOT_TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()

class WebAppDataFilter(Filter):
    async def __call__(self, message: types.Message, **kwds) -> Union[bool, Dict[str, Any]]:
        return dict(web_app_data=message.web_app_data) if message.web_app_data else False

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    caption = """Привет!
Мы команда профессионалов, создаём песни для героев, превращая их истории в музыку.

Вы можете подарить песню близкому на фронте или, находясь на передовой, передать его родным. Музыка навсегда увековечит историю и имя героя. 

Жми на старт – и мы создадим для вас песню"""
    photo = "https://storage.yandexcloud.net/patriot-music/svo_photo.jpg"
    wab_app_url = "https://skyrodev.ru"
    kb = [[types.KeyboardButton(text="Test", web_app=types.WebAppInfo(url=wab_app_url))]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer_photo(photo=photo, caption=caption, reply_markup=keyboard)
    # await bot.get_chat_menu_button()
    # await bot.set_chat_menu_button(chat_id=message.chat.id, menu_button=types.MenuButtonWebApp(text="Start", web_app=types.WebAppInfo(url="https://skyrodev.ru")))

async def invoice(message: types.Message, web_app_data: types.WebAppData):
    web_app_data = json.loads(web_app_data.data)
    price = [types.LabeledPrice(label="Pay", amount=int(web_app_data["prices"]) * 100)]
    # await bot.send_invoice(
    #     chat_id=message.chat.id,
    #     title=web_app_data["title"],
    #     description=web_app_data["description"],
    #     payload=web_app_data["payload"],
    #     currency=web_app_data["currency"],
    #     prices=price,
    #     provider_token="381764678:TEST:114933"
    # )
    

@app.post("/create-invoice")
async def create_invoice(web_app_data):
    web_app_data = json.loads(web_app_data)
    price = [types.LabeledPrice(label="Pay", amount=int(web_app_data["prices"]) * 100)]
    link = await bot.create_invoice_link(
        title=web_app_data["title"],
        description=web_app_data["description"],
        payload=web_app_data["payload"],
        currency=web_app_data["currency"],
        prices=price,
        provider_token="381764678:TEST:114933"
    )
    return link

async def start_server():
    from uvicorn import Config, Server
    config = Config("bot:app", port=8000, host="0.0.0.0", reload=True)
    server = Server(config)
    await server.serve()

async def start_bot():
    await dp.start_polling(bot)


async def main():
    
    # Запуск бота
    task1 = asyncio.create_task(start_bot())
    task2 = asyncio.create_task(start_server())
    await asyncio.gather(task1, task2)
    

if __name__ == "__main__":
    # if settings.ENVIRONMENT == "local":
    #     print(settings.BOT_TOKEN)
    # else:
    #     print("It's production")
    asyncio.run(main())
