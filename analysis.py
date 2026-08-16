import pandas as pd

def daily_returns(prices):
    return prices.pct_change().dropna()


def rolling_correlation(returns, col_a, col_b, window=60):
    return returns[col_a].rolling(window).corr(returns[col_b])


def normalise_to_100(prices):
    return prices / prices.iloc[0] * 100


def summary_stats(returns, trading_days=252):
    stats = pd.DataFrame({
        "ann_return_%": returns.mean() * trading_days * 100,
        "ann_vol_%": returns.std() * (trading_days ** 0.5) * 100,
        "sharpe_(rf=0)": (returns.mean() * trading_days) / (returns.std() * (trading_days ** 0.5)),
    })
    return stats.round(2)
