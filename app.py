from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "7025443798:AAHscYakT44DXSIyOHmNcP13dAMrwVZkQlk"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

@app.route('/')
def home():
    return "Bot is running"

@app.route(f'/{TELEGRAM_BOT_TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "👋 Welcome to PropertyGenie AI Bot!\n\nPlease tell me what kind of property you are looking for (buy/sell/rent) and in which city?")
        else:
            send_message(chat_id, "✅ Got your message! We’ll help you shortly.")

    return {"ok": True}
