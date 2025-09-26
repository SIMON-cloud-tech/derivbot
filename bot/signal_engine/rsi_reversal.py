import pandas as pd
from bot.signal_engine.utils import fetch_candles, calculate_rsi

def generate_signal(tick, current_position):
    candles = fetch_candles()
    if candles is None or len(candles) < 15:
        return None, None

    df = pd.DataFrame(candles)
    df['rsi'] = calculate_rsi(df['close'], window=14)
    rsi = df['rsi'].iloc[-1]

    if rsi < 30 and current_position != "long":
        return "BUY", f"RSI is {rsi:.2f} — oversold zone"
    elif rsi > 70 and current_position != "short":
        return "SELL", f"RSI is {rsi:.2f} — overbought zone"
    else:
        return None, None
