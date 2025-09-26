import pandas as pd
from bot.signal_engine.utils import fetch_candles, calculate_sma

def generate_signal(tick, current_position):
    # Fetch recent candle data
    candles = fetch_candles()
    if candles is None or len(candles) < 20:
        return None, None

    df = pd.DataFrame(candles)
    df['sma_fast'] = calculate_sma(df['close'], window=5)
    df['sma_slow'] = calculate_sma(df['close'], window=15)

    # Check for crossover
    if df['sma_fast'].iloc[-2] < df['sma_slow'].iloc[-2] and df['sma_fast'].iloc[-1] > df['sma_slow'].iloc[-1]:
        return "BUY", "Fast SMA crossed above slow SMA — bullish signal"
    elif df['sma_fast'].iloc[-2] > df['sma_slow'].iloc[-2] and df['sma_fast'].iloc[-1] < df['sma_slow'].iloc[-1]:
        return "SELL", "Fast SMA crossed below slow SMA — bearish signal"
    else:
        return None, None
