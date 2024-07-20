import yfinance as yf
import pandas as pd
import os
from datetime import datetime, timedelta

def download_data_chunk(ticker, start, end, interval="1h"):
    try:
        data = yf.download(ticker, start=start, end=end, interval=interval)
        return data
    except Exception as e:
        print(f"Failed to download data for {ticker}: {e}")
        return None

def download_and_save_data(ticker, start, end, interval="1h", folder="data"):
    current_start = pd.to_datetime(start)
    current_end = current_start + timedelta(days=60)
    final_end = pd.to_datetime(end)

    all_data = pd.DataFrame()

    while current_start < final_end:
        if current_end > final_end:
            current_end = final_end
        print(f"Downloading data for {ticker} from {current_start} to {current_end}")
        data_chunk = download_data_chunk(ticker, current_start.strftime("%Y-%m-%d"), current_end.strftime("%Y-%m-%d"), interval)
        if data_chunk is not None:
            all_data = pd.concat([all_data, data_chunk])
        current_start = current_end
        current_end = current_start + timedelta(days=60)

    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, f"{ticker}_{interval}_{start}_to_{end}.csv")
    all_data.to_csv(file_path)
    return file_path

# Parameters
tickers = ["XAUUSD=X", "EURUSD=X", "JPYUSD=X"]  # Forex pairs
start_date = "2022-01-01"
end_date = pd.Timestamp.now().strftime("%Y-%m-%d")

# Download and save data for each ticker
for ticker in tickers:
    file_path = download_and_save_data(ticker, start=start_date, end=end_date, interval="1h")
    print(f"Data saved to {file_path}")
