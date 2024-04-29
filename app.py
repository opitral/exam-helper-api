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


@app.get("/tap")
async def single_tap():
    bot.send_message(helper, "Да")
    return {"message": "single tap"}


@app.get("/doubleTap")
async def double_tap():
    bot.send_message(helper, "Не")
    return {"message": "tap"}


@app.get("/up")
async def single_up():
    bot.send_message(helper, "Наступне питання")
    return {"message": "single up"}


@app.get("/down")
async def single_down():
    bot.send_message(helper, "Попереднє питання")
    return {"message": "single down"}


@app.get("/right")
async def single_right():
    bot.send_message(helper, "Наступне речення")
    return {"message": "single right"}


@app.get("/left")
async def single_left():
    bot.send_message(helper, "Прочитай речення з початку")
    return {"message": "single left"}


@app.get("/doubleLeft")
async def double_left():
    bot.send_message(helper, "Прочитай повністю з початку")
    return {"message": "double left"}


@app.get("/doubleRight")
async def double_right():
    bot.send_message(helper, "медний бичок")
    return {"message": "double right"}


@app.get("/doubleDown")
async def double_down():
    bot.send_message(helper, "Дай більше інфи (gpt, google)")
    return {"message": "double down"}


@app.get("/doubleUp")
async def double_up():
    bot.send_message(helper, "1488")
    return {"message": "double up"}


@app.get("/deploy")
async def deploy():
    subprocess.run('sh deploy.sh', shell=True)
    return {"message": "deployed"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=1488, log_level="info")
