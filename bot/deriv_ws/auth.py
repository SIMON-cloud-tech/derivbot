import websocket
import json
from bot.config import DERIV_TOKEN

def verify_token():
    def on_message(ws, message):
        print("🔐 Auth response:", message)
        ws.close()

    def on_open(ws):
        ws.send(json.dumps({"authorize": DERIV_TOKEN}))

    ws = websocket.WebSocketApp(
        "wss://ws.derivws.com/websockets/v3",
        on_open=on_open,
        on_message=on_message
    )
    ws.run_forever()
