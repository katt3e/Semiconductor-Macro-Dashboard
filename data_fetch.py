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

#Pulling the risk free rate from 13week US Treasury Bills (most common method). 
#If there's an error, return to 0.0 so that the sharpe ratio is computed anyways
def fetch_risk_free_rate(ticker="^IRX"):
    try:
        quote = yf.Ticker(ticker).history(period="5d")
        if quote.empty:
            return 0.0
        latest_yield_pct = quote["Close"].iloc[-1]
        return latest_yield_pct / 100
    except Exception:
        return 0.0
