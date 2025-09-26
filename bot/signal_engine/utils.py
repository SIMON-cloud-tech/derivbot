import numpy as np
import requests
from bot.config import DERIV_TOKEN, ASSET_SYMBOL

def fetch_candles():
    url = "https://api.deriv.com/v2"
    payload = {
        "req_id": 1,
        "candles": ASSET_SYMBOL,
        "end": "latest",
        "count": 50,
        "granularity": 60,
        "subscribe": 0,
        "authorize": DERIV_TOKEN
    }
    try:
        response = requests.post(f"{url}/candles", json=payload)
        data = response.json()
        return data.get("candles")
    except Exception as e:
        print("❌ Candle fetch error:", e)
        return None

def calculate_sma(series, window):
    return series.rolling(window=window).mean()

def calculate_rsi(series, window=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))
