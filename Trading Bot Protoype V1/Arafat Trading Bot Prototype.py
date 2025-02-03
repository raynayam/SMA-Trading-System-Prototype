import requests
import pandas as pd
import time

# Tradovate API endpoint for authentication
url = "https://demo.tradovateapi.com/v1"
url = "https://md.tradovateapi.com/"
# Replace with your credentials
API_KEY = "your_api_key"
USERNAME = "BOT_TEST"
PASSWORD = "your_password"
ACCOUNT_ID = "your_account_id"

# Authentication
AUTH_URL = "https://api.tradovate.com/v1/auth/oauth/token"

def get_auth_token():
    response = requests.post(AUTH_URL, data={
        "grant_type": "password",
        "username": USERNAME,
        "password": PASSWORD,
        "client_id": API_KEY
    })
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Authentication failed: {response.text}")

# Fetch historical data
def fetch_historical_data(symbol, timeframe="1min", start="2023-01-01", end="2023-12-31"):
    token = get_auth_token()
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "symbol": symbol,
        "interval": timeframe,
        "start": start,
        "end": end
    }
    response = requests.get("https://api.tradovate.com/v1/data/historical", headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.text}")

# Calculate SMA
def calculate_sma(data, window=20):
    df = pd.DataFrame(data)
    df['SMA'] = df['close'].rolling(window=window).mean()
    return df

# Trading logic
def trading_logic(data):
    latest_close = data['close'].iloc[-1]
    latest_sma = data['SMA'].iloc[-1]
    
    if latest_close > latest_sma:
        print("BUY signal")
        place_order("MNQ", "Buy", 1)  # Buy 1 contract
    elif latest_close < latest_sma:
        print("SELL signal")
        place_order("MNQ", "Sell", 1)  # Sell 1 contract

# Place order
def place_order(symbol, action, quantity):
    token = get_auth_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    order_data = {
        "accountId": ACCOUNT_ID,
        "action": action,
        "symbol": symbol,
        "orderType": "Market",
        "1": quantity
    }
    response = requests.post("https://api.tradovate.com/v1/order/placeorder", headers=headers, json=order_data)
    if response.status_code == 200:
        print("Order placed successfully:", response.json())
    else:
        raise Exception(f"Failed to place order: {response.text}")

# Main loop
def main():
    symbol = "MNQ"  # E-mini S&P 500 futures
    while True:
        data = fetch_historical_data(symbol)
        data_with_sma = calculate_sma(data)
        trading_logic(data_with_sma)
        time.sleep(240)  # Run every 60 seconds

if __name__ == "__main__":
    main()