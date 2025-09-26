from telethon import TelegramClient
from bot.config import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_RECIPIENT
from bot.notifier.formatter import format_message

# Create Telegram client session
client = TelegramClient("glowradar_session", TELEGRAM_API_ID, TELEGRAM_API_HASH)

async def send_telegram_message(signal, justification):
    """
    Sends a Telegram message with the trading signal and its justification.
    """
    message_body = format_message(signal, justification)
    await client.send_message(TELEGRAM_RECIPIENT, message_body)
    print("✅ Telegram sent:", message_body)
