import os
import requests

API = "https://openrouter.ai/api/v1/chat/completions"

KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL")


def ask_ai(text):

    headers = {
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": text}
        ],
    }

    r = requests.post(API, headers=headers, json=data)

    if r.status_code != 200:
        return "AI error"

    return r.json()["choices"][0]["message"]["content"]
