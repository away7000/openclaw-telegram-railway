def run_tool(text):

    if text.startswith("/ping"):
        return "pong"

    if text.startswith("/time"):
        import time
        return str(time.time())

    return None
