
# 🚀 Crypto Trading CLI Bot

A production-ready **Command Line Interface (CLI) trading bot** built using Python that interacts with Binance Futures API to place and manage orders.

---

## 📌 Project Overview

This project allows users to execute crypto trades directly from the terminal using a clean and structured CLI interface.

It includes:

* ✅ Order placement (MARKET & LIMIT)
* ✅ Input validation
* ✅ Retry mechanism for reliability
* ✅ Clean CLI output (user-friendly)
* ✅ File-based logging (no console noise)
* ✅ Secure API key handling using `.env`

---

## ⚙️ Tech Stack

* **Python 3.11+**
* **Typer** → CLI framework
* **Rich** → Beautiful terminal output
* **Binance API** → Trading execution
* **Tenacity** → Retry handling
* **python-dotenv** → Environment variables

---

## 📁 Project Structure

```
TRADING/
│── bot/
│   ├── client.py          # Binance client setup
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── exceptions.py      # Custom exceptions
│   ├── logger.py          # Logger setup
│   
│
│── cli.py                 # CLI entry point
│── config.py              # Configurations
│── .env                   # API keys (not pushed)
│── .gitignore             # Ignore sensitive files
│── bot.log            # Logs file
```

---

## 🔐 Environment Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Create `.env` File

Create a file in the root folder:

```
.env
```

Add your API keys:

```
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_secret_key
```

---

### 🔒 Important

Never upload `.env` to GitHub.

Create `.gitignore`:

```
.env
venv/
__pycache__/
bot.log
```

---

## 🔑 Binance Setup (Testnet Recommended)

1. Create API keys from Binance Futures Testnet
2. Enable:

   * ✅ Futures Trading
3. Add test balance (USDT)
4. Use **Testnet base URL** in your client

---

## ▶️ Usage

### 🔹 Place Market Order

```bash
python cli.py trade place --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

---

### 🔹 Place Limit Order

```bash
python cli.py trade place --symbol BTCUSDT --side BUY --order-type LIMIT --quantity 0.001 --price 75000
```

---

## 🧾 Sample Output

```
╭──────────────────────────────────╮
│ Placing MARKET order for BTCUSDT │
╰──────────────────────────────────╯

Order Request:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

Order Response:
Order ID: 13060557669
Status: FILLED
Executed Quantity: 0.0010
Average Price: 77840.30

✅ Order executed successfully
```

---

## 📊 Logging

* Logs are stored in:

```
bot.log
```

* Includes:

  * Request details
  * API responses
  * Order status updates
  * Errors (if any)

---

## 🔁 Retry Mechanism

* Automatically retries failed API calls
* Config:

  * Max attempts: **3**
  * Delay: **2 seconds**

---

## ❗ Error Handling

Custom exceptions:

* `ValidationError` → Invalid user input
* `OrderError` → API/order failure

---

## ✅ Features Summary

* Clean CLI design
* Secure API handling
* Reliable execution with retries
* Structured logging
* Production-style architecture

---

## 🚧 Future Improvements

* Add Stop Loss / Take Profit
* Position management
* Web dashboard (Streamlit)
* Strategy-based trading
* Backtesting module

---
live demo : 
## 👨‍💻 Author

Revan Kumar Battini

Built as part of a real-world trading system assignment to demonstrate:

* CLI design
* API integration
* Clean architecture
* Production-level practices

---

## ⚠️ Disclaimer

This project is for educational purposes only.
Trading cryptocurrencies involves risk — use cautiously.

---
