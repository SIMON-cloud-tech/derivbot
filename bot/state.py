class BotState:
    def __init__(self):
        self.last_signal = None     # Last signal sent (e.g., "BUY")
        self.position = None        # Current market stance ("long", "short", or None)

    def should_notify(self, new_signal):
        """
        Returns True if the new signal is different from the last one.
        Prevents duplicate WhatsApp messages.
        """
        if new_signal != self.last_signal:
            self.last_signal = new_signal
            return True
        return False

    def update_position(self, signal):
        """
        Updates the bot's internal position state based on the signal.
        """
        if signal == "BUY":
            self.position = "long"
        elif signal == "SELL":
            self.position = "short"
        elif signal == "EXIT":
            self.position = None
