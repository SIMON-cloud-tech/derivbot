deriv-trading-bot/
│
├── client/                      # Frontend trigger
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
├── bot/                         # Core bot logic
│   ├── __init__.py
│   ├── config.py                # Deriv token, asset config
│   ├── runner.py                # Main loop (1-second interval)
│   ├── state.py                 # Signal memory, debounce
│   ├── deriv_ws/                # Deriv WebSocket integration
│   │   ├── __init__.py
│   │   ├── stream.py            # Live tick/candle stream
│   │   └── auth.py              # Token auth
│   ├── signal_engine/           # Signal strategies
│   │   ├── __init__.py
│   │   ├── sma_crossover.py
│   │   ├── rsi_reversal.py
│   │   └── utils.py
│   └── notifier/                # WhatsApp notifications
│       ├── __init__.py
│       ├── whatsapp.py
│       └── formatter.py
│
├── server/                      # Backend trigger
│   ├── app.py
│   └── background.py
│
├── utils/                       # Shared helpers
│   ├── logger.py
│   └── timer.py
│
├── tests/                       # Unit tests
│   ├── test_deriv_ws.py
│   ├── test_signals.py
│   └── test_notifier.py
│
├── requirements.txt
└── README.md
