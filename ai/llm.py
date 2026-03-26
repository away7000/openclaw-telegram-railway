import os
import requests

API = "https://openrouter.ai/api/v1/chat/completions"

KEY = os.getenv("OPENROUTER_API_KEY")

MODEL = os.getenv(
    "MODEL",
    "deepseek/deepseek-chat"
)


def ask_ai(text):

    if not KEY:
        return "No API key"

    headers = {
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://railway.app",
        "X-Title": "railway-bot"
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": text
            }
        ],
        "max_tokens": 500
    }

    try:

        r = requests.post(
            API,
            headers=headers,
            json=data,
            timeout=60
        )

        print("STATUS:", r.status_code)
        print("RESP:", r.text)

        if r.status_code != 200:
            return r.text

        j = r.json()

        return j["choices"][0]["message"]["content"]

    except Exception as e:
        return str(e)
