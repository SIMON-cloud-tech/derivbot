from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Deriv API token for authentication
DERIV_TOKEN = os.getenv("DERIV_TOKEN")

# Asset symbol to analyze (e.g., USD/JPY)
ASSET_SYMBOL = "frxUSDJPY"

# Interval between bot cycles (in seconds)
POLL_INTERVAL = 1
#telegram credentials
TELEGRAM_API_ID = int(os.getenv("TELEGRAM_API_ID"))
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
TELEGRAM_RECIPIENT = os.getenv("TELEGRAM_RECIPIENT")
