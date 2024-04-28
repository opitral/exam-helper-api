from os import getenv
from dotenv import load_dotenv
from fastapi import FastAPI
from telebot import TeleBot

load_dotenv()
app = FastAPI()
bot = TeleBot(getenv("TELEGRAM_BOT_TOKEN"))
helper = getenv("TELEGRAM_HELPER_ID")


@app.get("/up")
async def move_up():
    print("up")
    bot.send_message(helper, "up")
    return {"message": "Moving up!"}


@app.get("/down")
async def move_down():
    print("down")
    bot.send_message(helper, "down")
    return {"message": "Moving down!"}


@app.get("/right")
async def move_right():
    print("right")
    bot.send_message(helper, "right")
    return {"message": "Moving right!"}


@app.get("/left")
async def move_left():
    print("left")
    bot.send_message(helper, "left")
    return {"message": "Moving left!"}


@app.get("/tap")
async def move_left():
    print("tap")
    bot.send_message(helper, "tap")
    return {"message": "Tap!"}