import time


def call_function(name, args):

    if name == "get_time":
        return str(time.time())

    if name == "ping":
        return "pong"

    return "unknown function"
