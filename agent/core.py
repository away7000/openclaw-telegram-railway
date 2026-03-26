from agent.llm import ask_llm
from agent.tools import call_function
from agent.memory import add, get


def load_skill():

    try:
        with open("skill.md", "r") as f:
            return f.read()
    except:
        return ""


MAX_STEPS = 5


def run_agent(user, text):

    skill = load_skill()

    add(user, text)

    mem = get(user)

    messages = []

    # system prompt
    messages.append({
        "role": "system",
        "content": skill
    })

    for m in mem:
        messages.append({
            "role": "user",
            "content": m
        })

    for step in range(MAX_STEPS):

        r = ask_llm(messages)

        msg = r["choices"][0]["message"]

        messages.append(msg)

        # ✅ TOOL CALL
        if "tool_calls" in msg:

            call = msg["tool_calls"][0]

            name = call["function"]["name"]

            args = call["function"].get("arguments", {})

            result = call_function(name, args)

            messages.append({
                "role": "tool",
                "tool_name": name,
                "content": str(result)
            })

            continue

        # ✅ FINAL ANSWER
        if "content" in msg and msg["content"]:

            reply = msg["content"]

            add(user, reply)

            return reply

    return "Agent stopped"
