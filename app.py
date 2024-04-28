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
    bot.send_message(helper, "Нахил вверх")
    return {"message": "Moving up!"}


@app.get("/down")
async def move_down():
    bot.send_message(helper, "Нахил вниз")
    return {"message": "Moving down!"}


@app.get("/right")
async def move_right():
    bot.send_message(helper, "Нахил вправо")
    return {"message": "Moving right!"}


@app.get("/left")
async def move_left():
    bot.send_message(helper, "Нахил вліво")
    return {"message": "Moving left!"}


@app.get("/tap")
async def move_left():
    bot.send_message(helper, "Тап по екрану")
    return {"message": "Tap!"}


@app.get("/deploy")
async def deploy():
    subprocess.run('sh deploy.sh', shell=True)
    return {"message": "Deployed! 123"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=1488, log_level="info")
