# Semiconductor & Macro Dashboard

A small Python tool that pulls price data for key semiconductor names
(ASML, TSM, NVDA) alongside the SOXX ETF (a proxy for the broader
Philadelphia Semiconductor Index), and produces:

- **Rebased performance chart** — how each name has moved relative to the
  index over the last 2 years, indexed to 100 at the start date.
- **60-day rolling correlation** between ASML (equipment/lithography) and
  SOXX (the broad index) — a way of seeing whether the "supply chain
  bottleneck" name moves in or out of step with the sector as a whole.
- **Annualised return, volatility, and Sharpe ratio** for each ticker,
  saved to `output/summary_stats.csv`.

This was built to support quantitative analysis behind
[kat3markets](#) (Substack), specifically the semiconductor supply chain
and capital markets themes covered there — ASML's EUV lithography
monopoly, TSMC's foundry dominance, and how AI-driven demand (proxied by
NVDA) feeds through to the sector.

## Why these tickers

| Ticker | Role in the supply chain |
|---|---|
| ASML   | Sole supplier of EUV lithography machines — the bottleneck at the top of the chain |
| TSM    | Dominant foundry, converts designs into physical chips |
| NVDA   | Demand-side proxy — AI/compute driven chip demand |
| SOXX   | Broad semiconductor index, used as the benchmark |

## Setup

```bash
git clone https://github.com/katt3e/semiconductor-macro-dashboard.git
cd semiconductor-macro-dashboard
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Output (charts + CSV) is saved to `output/`.

## Project structure

```
semiconductor-macro-dashboard/
├── main.py          # orchestrates the pipeline: fetch -> analyse -> plot
├── data_fetch.py     # yfinance wrapper for pulling price data
├── analysis.py       # returns, rolling correlation, normalisation, summary stats
├── requirements.txt
└── output/           # generated charts and stats (created on run)
```

## Possible extensions

- Add a macro layer (e.g. Fed funds rate or 10y yield via `fredapi`) to
  test correlation between rate expectations and semiconductor equity
  performance.
- Extend the ticker list to cover ASM International, Applied Materials,
  or SMIC as further points on the supply chain.
- Turn the rolling correlation chart into a signal (e.g. flag periods
  where correlation breaks down) as a lightweight event-detection layer.

## Author

Katarzyna Koczar — [kat3markets Substack](#) | [GitHub](https://github.com/katt3e)
