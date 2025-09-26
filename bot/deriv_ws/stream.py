import websocket
import json
from bot.config import DERIV_TOKEN, ASSET_SYMBOL

latest_tick = None  # Shared variable to hold the most recent tick

def on_open(ws):
    # Authenticate with Deriv API
    ws.send(json.dumps({"authorize": DERIV_TOKEN}))
    # Subscribe to live tick data for the selected asset
    ws.send(json.dumps({"ticks": ASSET_SYMBOL, "subscribe": 1}))

def on_message(ws, message):
    global latest_tick
    data = json.loads(message)

    # Extract tick data if available
    if "tick" in data:
        latest_tick = data["tick"]["quote"]

def get_latest_tick():
    return latest_tick

def start_stream():
    ws = websocket.WebSocketApp(
        "wss://ws.derivws.com/websockets/v3",
        on_open=on_open,
        on_message=on_message
    )
    ws.run_forever()
