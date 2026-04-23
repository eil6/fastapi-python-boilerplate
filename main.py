from fastapi import FastAPI, Request
import os
import requests

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.get("/")
def home():
    return {"status": "bot running"}

@app.post("/api/telegram")
async def telegram(request: Request):
    data = await request.json()

    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "")

    if chat_id and text:
        requests.post(
            f"{API}/sendMessage",
            json={"chat_id": chat_id, "text": f"You said: {text}"}
        )

    return {"ok": True}