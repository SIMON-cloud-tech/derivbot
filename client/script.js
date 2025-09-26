document.getElementById("startBot").addEventListener("click", async () => {
  const status = document.getElementById("status");
  status.textContent = "⏳ Starting bot...";

  try {
    const response = await fetch("http://localhost:8000/start-bot", {
      method: "POST"
    });

    if (response.ok) {
      status.textContent = "✅ Bot started successfully!";
    } else {
      status.textContent = "❌ Failed to start bot.";
    }
  } catch (error) {
    console.error("Error:", error);
    status.textContent = "⚠️ Error connecting to server.";
  }
});
