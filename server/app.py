from fastapi import FastAPI
from server.background import start_bot

app = FastAPI()

@app.post("/start-bot")
def trigger_bot():
    """
    Endpoint to start the trading bot.
    Called by the frontend when user clicks 'Start Bot'.
    """
    start_bot()
    return {"status": "Bot started"}
