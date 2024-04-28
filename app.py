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


@app.get("/deploy")
async def deploy():
    # os.system('''
    #     cd ~/exam-helper-bot;
    #     git pull;
    #     pm2 restart exam;
    #     cd ~/exam-helper-api;
    #     git pull;
    #     pm2 restart 1488;
    # ''')

    # subprocess.run(['sh ~/exam-hepler-api/deploy.sh'])
    # subprocess.run(['git', 'pull'])
    # subprocess.run(['pm2', 'restart exam'])
    # subprocess.run(['cd', '~/exam-helper-api'])
    # subprocess.run(['git', 'pull'])
    # subprocess.run(['pm2', 'restart 1488'])
    process = subprocess.run('sh deploy.sh', shell=True) 


    return {"message": "Deployed!"}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=1488, log_level="info")
