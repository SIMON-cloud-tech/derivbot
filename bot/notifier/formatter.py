from datetime import datetime

def format_message(signal, justification):
    """
    Formats the Telegram message with timestamp, signal, and reason.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (
        f"📡 Deriv Signal Alert\n"
        f"🕒 {timestamp}\n"
        f"📊 Action: {signal}\n"
        f"🧠 Reason: {justification}"
    )
