import yfinance as yf
import pandas as pd


def fetch_prices(tickers, period="2y", interval="1d"):
    
    #Download adjusted close prices for the chosen tickers.

    raw = yf.download(tickers, period=period, interval=interval, auto_adjust=True, progress=False)

    # yfinance returns a MultiIndex column DataFrame for multiple tickers,
    # and a plain DataFrame for a single ticker. Normalise both.

    if isinstance(raw.columns, pd.MultiIndex):
        data = raw["Close"]
    else:
        data = raw[["Close"]]
        data.columns = tickers

    return data.dropna(how="all")


def fetch_single(ticker, period="2y", interval="1d"):
    return fetch_prices([ticker], period=period, interval=interval)
