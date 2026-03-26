import os
import requests

API = "https://openrouter.ai/api/v1/chat/completions"

KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL", "deepseek/deepseek-chat")


def ask_llm(messages):

    headers = {
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://railway.app",
        "X-Title": "openclaw-agent"
    }

    data = {
        "model": MODEL,
        "messages": messages
    }

    r = requests.post(API, headers=headers, json=data)

    if r.status_code != 200:
        return r.text

    return r.json()["choices"][0]["message"]["content"]
