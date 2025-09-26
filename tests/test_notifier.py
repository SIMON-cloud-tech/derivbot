import unittest
from bot.notifier.formatter import format_message

class TestNotifier(unittest.TestCase):
    def test_format_message_structure(self):
        signal = "BUY"
        justification = "Fast SMA crossover detected"
        message = format_message(signal, justification)

        self.assertIn("📡 Deriv Signal Alert", message)
        self.assertIn("📊 Action: BUY", message)
        self.assertIn("🧠 Reason: Fast SMA crossover detected", message)

if __name__ == "__main__":
    unittest.main()
