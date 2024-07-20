# Forex Data Downloader

This script allows you to download historical Forex data for specified tickers using the `yfinance` library. The data is saved in hourly intervals as CSV files. This script handles downloading the data in chunks to avoid any limitations of the `yfinance` API.

## Requirements

- Python 3.x
- `yfinance` library
- `pandas` library

## Installation

1. **Clone the repository or download the script.**

2. **Install the required libraries:**
    ```bash
    pip install yfinance pandas
    ```

## Usage

### Parameters

- `tickers`: List of Forex pairs to download data for. Example: `["XAUUSD=X", "EURUSD=X", "JPYUSD=X"]`
- `start_date`: The start date for downloading data. Format: `YYYY-MM-DD`
- `end_date`: The end date for downloading data. Format: `YYYY-MM-DD`. Default is the current date.
- `interval`: The interval for the data. Default is `1h` (1 hour).
- `folder`: The folder where the CSV files will be saved. Default is `data`.