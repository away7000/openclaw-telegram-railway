from agent.llm import ask_llm
from agent.tools import call_function
from agent.memory import add, get


def run_agent(user, text):

    add(user, text)

    mem = get(user)

    messages = []

    for m in mem:
        messages.append({
            "role": "user",
            "content": m
        })

    r = ask_llm(messages)

    msg = r["choices"][0]["message"]

    # ✅ LLM call function
    if "tool_calls" in msg:

        call = msg["tool_calls"][0]

        name = call["function"]["name"]

        args = call["function"].get("arguments", {})

        result = call_function(name, args)

        messages.append(msg)

        messages.append({
            "role": "tool",
            "name": name,
            "content": result
        })

        r2 = ask_llm(messages)

        reply = r2["choices"][0]["message"]["content"]

    else:

        reply = msg["content"]

    add(user, reply)

    return reply
    
def load_skill():

    try:
        with open("skill.md", "r") as f:
            return f.read()
    except:
        return ""
