# AI-Powered Crypto Trading Bot 🤖📈

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview
A Python application that analyzes live cryptocurrency price data, applies AI/rule-based strategies to identify trade opportunities, simulates trades (paper trading), and runs inside a Docker container. Now supports real trading on Binance.

## Features
- Fetches live crypto prices from CoinGecko
- Implements a moving average crossover strategy
- Simulates trades and logs them to CSV
- Runs on a schedule (every 5–10 minutes)
- Fully containerized with Docker
- **Supports real trading on Binance (with API keys)**

## Quick Start

### Prerequisites
- Docker installed on your system
- Binance API key and secret (for real trading)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/r3d-net/AI-Powered-Crypto-Trading-Bot.git
   cd AI-Powered-Crypto-Trading-Bot
   ```

2. **Build Docker Image**
   ```bash
   docker build -t crypto-trading-bot .
   ```

3. **Run the Container**

   **Paper Trading (default):**
   ```bash
   docker run -d --name trading-bot crypto-trading-bot
   ```

   **Real Trading on Binance:**
   ```bash
   docker run -d --name trading-bot \
     -v "$(pwd)/logs":/app/logs \
     -e BINANCE_API_KEY=your_api_key \
     -e BINANCE_API_SECRET=your_api_secret \
     -e USE_BINANCE=1 \
     crypto-trading-bot
   ```

## Project Structure
```
app/
  __init__.py
  main.py
  config.py
  data_fetcher.py
  strategy.py
  trader.py
  binance_trader.py
  logger.py
logs/
  trades.csv (auto-created)
requirements.txt
Dockerfile
README.md
```

## Configuration

Edit `app/config.py` to customize:
- Trading symbol (default: Bitcoin)
- Trade amount (default: $100)
- Moving average windows
- Schedule interval

## View Logs
Trade logs are saved in `logs/trades.csv` on your host (if using the bind mount), or inside the container otherwise. To copy them out manually:
```bash
docker cp trading-bot:/app/logs/trades.csv ./trades.csv
```

## Security Best Practices
- **Never share your Binance API key or secret.**
- Use API keys with only the permissions you need (e.g., trading only, no withdrawal).
- Delete or regenerate your API key if it is ever exposed.
- Test thoroughly in paper trading mode before enabling real trading.

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Extensions
- Real trading via other exchange APIs (Coinbase, etc.)
- Telegram/Discord alerts for trade signals
- Advanced AI/ML strategies (sentiment analysis, RL, etc.)
- Web dashboard for monitoring
- Multi-asset and multi-strategy support

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer
This software is for educational purposes only. Use at your own risk. The authors are not responsible for any financial losses incurred through the use of this software. 
