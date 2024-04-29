from os import getenv
from dotenv import load_dotenv
from fastapi import FastAPI
from telebot import TeleBot
import uvicorn

import subprocess

load_dotenv()
app = FastAPI()
bot = TeleBot(getenv("TELEGRAM_BOT_TOKEN"))
helper = getenv("TELEGRAM_HELPER_ID")


@app.get("/up")
async def move_up():
    bot.send_message(helper, "Наступне питання")
    return {"message": ""}


@app.get("/down")
async def move_down():
    bot.send_message(helper, "Не / Нехай gpt дасть більше інфи по питанню")
    return {"message": "down"}


@app.get("/right")
async def move_right():
    bot.send_message(helper, "Наступне речення")
    return {"message": "right"}


@app.get("/left")
async def move_left():
    bot.send_message(helper, "Прочитай речення з початку")
    return {"message": "left"}


@app.get("/tap")
async def move_left():
    bot.send_message(helper, "Да / Почни читати відповідь з початку")
    return {"message": "tap"}


@app.get("/deploy")
async def deploy():
    subprocess.run('sh deploy.sh', shell=True)
    return {"message": "deployed"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=1488, log_level="info")
