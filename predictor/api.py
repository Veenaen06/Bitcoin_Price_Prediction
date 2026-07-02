import requests

# Binance API for current price
CURRENT_PRICE_URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

# Binance API for historical daily candles
HISTORICAL_URL = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=60"


def get_current_bitcoin_price():
    """
    Returns current Bitcoin price.
    """

    try:
        response = requests.get(CURRENT_PRICE_URL, timeout=10)
        response.raise_for_status()

        data = response.json()

        return float(data["price"])

    except Exception as e:
        print("Current Price Error:", e)
        return None


def get_last_60_close_prices():
    """
    Returns last 60 daily closing prices.
    """

    try:
        response = requests.get(HISTORICAL_URL, timeout=10)
        response.raise_for_status()

        candles = response.json()

        close_prices = []

        for candle in candles:
            close_prices.append(float(candle[4]))

        return close_prices

    except Exception as e:
        print("Historical Price Error:", e)
        return []