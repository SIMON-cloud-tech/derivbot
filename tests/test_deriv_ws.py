import unittest
from bot.deriv_ws.stream import get_latest_tick

class TestDerivWS(unittest.TestCase):
    def test_tick_initial_none(self):
        tick = get_latest_tick()
        self.assertIsNone(tick)

if __name__ == "__main__":
    unittest.main()
