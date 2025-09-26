import time
import asyncio
from bot.config import POLL_INTERVAL
from bot.state import BotState
from bot.deriv_ws.stream import get_latest_tick
from bot.signal_engine.sma_crossover import generate_signal
from bot.notifier.telegram import send_telegram_message
from bot.notifier.telegram import client  # Import the Telethon client

# Initialize bot state
state = BotState()

async def run_bot():
    print("🟢 Bot started.")
    await client.start()  # Start Telegram session

    while True:
        tick = get_latest_tick()

        if tick:
            signal, justification = generate_signal(tick, state.position)

            if signal and state.should_notify(signal):
                await send_telegram_message(signal, justification)
                state.update_position(signal)

        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    asyncio.run(run_bot())
