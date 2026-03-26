import os
import requests

from agent.functions import functions

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
        "messages": messages,
        "tools": functions,
        "tool_choice": "auto"
    }

    r = requests.post(API, headers=headers, json=data)

    print(r.text)

    return r.json()
