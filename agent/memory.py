memory = {}


def add(user, text):

    if user not in memory:
        memory[user] = []

    memory[user].append(text)

    memory[user] = memory[user][-10:]


def get(user):

    return memory.get(user, [])
