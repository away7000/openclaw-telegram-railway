from agent.memory import add, get
from agent.tools import run_tool
from agent.llm import ask_llm


def run_agent(user, text):

    tool = run_tool(text)

    if tool:
        return tool

    add(user, text)

    mem = get(user)

    messages = []

    for m in mem:
        messages.append({
            "role": "user",
            "content": m
        })

    reply = ask_llm(messages)

    add(user, reply)

    return reply
