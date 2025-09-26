import unittest
from bot.signal_engine.utils import calculate_sma, calculate_rsi
import pandas as pd

class TestSignals(unittest.TestCase):
    def test_sma_calculation(self):
        data = pd.Series([1, 2, 3, 4, 5])
        sma = calculate_sma(data, window=3)
        self.assertAlmostEqual(sma.iloc[-1], 4.0)

    def test_rsi_calculation(self):
        data = pd.Series([45, 46, 47, 46, 45, 44, 43, 42, 41, 40, 41, 42, 43, 44, 45])
        rsi = calculate_rsi(data, window=14)
        self.assertTrue(0 <= rsi.iloc[-1] <= 100)

if __name__ == "__main__":
    unittest.main()
