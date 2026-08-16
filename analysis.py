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
    
#once again, rfr defaults to 0.0 if not found
def summary_stats(returns, trading_days=252, risk_free_rate=0.0):
    ann_return = returns.mean() * trading_days
    ann_vol = returns.std() * (trading_days ** 0.5)
    stats = pd.DataFrame({
        "ann_return_%": ann_return * 100,
        "ann_vol_%": ann_vol * 100,
        f"sharpe_(rf={risk_free_rate:.1%})": (ann_return - risk_free_rate) / ann_vol,
    })
    return stats.round(2)
