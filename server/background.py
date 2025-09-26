import threading
from bot.runner import run_bot
from bot.deriv_ws.stream import start_stream

def start_bot():
    """
    Starts the WebSocket stream and bot loop in background threads.
    Prevents blocking the FastAPI server.
    """
    stream_thread = threading.Thread(target=start_stream, daemon=True)
    bot_thread = threading.Thread(target=run_bot, daemon=True)

    stream_thread.start()
    bot_thread.start()
