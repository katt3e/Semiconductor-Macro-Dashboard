import os
import matplotlib
matplotlib.use("Agg")  # rasterize plots to files, no display required
import matplotlib.pyplot as plt

from data_fetch import fetch_prices, fetch_risk_free_rate
from analysis import daily_returns, rolling_correlation, normalise_to_100, summary_stats

TICKERS = ["ASML", "TSM", "NVDA", "MU", "TXN", "SOXX"]
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output") #just the output folder, all graphs there


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Fetching price data...")
    prices = fetch_prices(TICKERS, period="2y")

    if prices.empty:
        print("No data returned. Check your internet connection or ticker list.")
        return

    returns = daily_returns(prices)

    print("Fetching current risk-free rate (3-month T-bill, ^IRX)...")
    risk_free_rate = fetch_risk_free_rate()
    print(f"Risk-free rate: {risk_free_rate:.2%}")

    print("\n          Annualised Summary Stats (2y)")
    stats = summary_stats(returns, risk_free_rate=risk_free_rate)
    print(stats)
    stats.to_csv(f"{OUTPUT_DIR}/summary_stats.csv")

    # Chart 1: Normalised Performance   
    norm = normalise_to_100(prices)
    plt.figure(figsize=(10, 6))
    for col in norm.columns:
        plt.plot(norm.index, norm[col], label=col)
    plt.title("Semiconductor Names vs SOXX, Rebased to 100")
    plt.ylabel("Indexed price (start = 100)")
    plt.margins(x=0)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/normalised_performance.png", dpi=150)
    plt.close()

    # Chart 2: rolling instead of static correlation, ASML vs SOXX 
    if "ASML" in returns.columns and "SOXX" in returns.columns:
        corr = rolling_correlation(returns, "ASML", "SOXX", window=60)
        plt.figure(figsize=(10, 4))
        plt.plot(corr.index, corr.values)
        plt.title("60-Day Rolling Correlation: ASML vs SOXX")
        plt.ylabel("Correlation")
        plt.ylim(bottom=0)
        plt.axhline(0, color="grey", linewidth=0.8)
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/rolling_correlation_asml_soxx.png", dpi=150)
        plt.close()

    # Chart 3: rolling correlation, MU vs SOXX 
    if "MU" in returns.columns and "SOXX" in returns.columns:
        corr_mu = rolling_correlation(returns, "MU", "SOXX", window=60)
        plt.figure(figsize=(10, 4))
        plt.plot(corr_mu.index, corr_mu.values, color="darkorange")
        plt.title("60-Day Rolling Correlation: MU vs SOXX")
        plt.ylabel("Correlation")
        plt.ylim(bottom=0)
        plt.axhline(0, color="grey", linewidth=0.8)
        plt.tight_layout()
        plt.savefig(f"{OUTPUT_DIR}/rolling_correlation_mu_soxx.png", dpi=150)
        plt.close()

    print(f"\nDone. Charts and stats saved to ./{OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
