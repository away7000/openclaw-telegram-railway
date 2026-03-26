import os
import requests

API = "https://openrouter.ai/api/v1/chat/completions"

KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = os.getenv(
    "MODEL",
    "mistralai/mistral-7b-instruct"
)


def ask_ai(text):

    if not KEY:
        return "No API key"

    headers = {
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://railway.app",
        "X-Title": "telegram-bot"
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": text
            }
        ]
    }

    try:

        r = requests.post(
            API,
            headers=headers,
            json=data,
            timeout=30
        )

        print(r.text)

        if r.status_code != 200:
            return f"API error {r.status_code}"

        j = r.json()

        return j["choices"][0]["message"]["content"]

    except Exception as e:
        return str(e)
