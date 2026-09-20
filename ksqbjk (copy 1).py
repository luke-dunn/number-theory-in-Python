import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date

def grab_stats(etoro_username):
    url = f"https://www.etoro.com/people/{etoro_username}/stats"
    try:
        html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        html.raise_for_status()  # Raise an error for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {etoro_username}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error
    
    soup = BeautifulSoup(html.text, "html.parser")
    
    # Monthly return data extraction
    cells = soup.find_all("div", attrs={"data-e2e": "stats-monthly-cell"})
    month_returns = {}
    for c in cells:
        m = re.search(r"(\d{4})\s+([A-Za-z]{3})", c["aria-label"])
        if m:
            yyyy, mmm = m.groups()
            pct = float(c.text.replace("%", "")) / 100
            month_returns[f"{yyyy}-{mmm}"] = pct

    # Extract risk and assets under copy (AUC)
    try:
        risk = float(soup.select_one('[data-e2e="risk-score-value"]').text)
        auc = float(soup.select_one('[data-e2e="assets-under-copy"]').text.replace("$", "").replace(",", ""))
    except AttributeError as e:
        print(f"Error extracting financial data for {etoro_username}: {e}")
        return pd.DataFrame()  # Return empty if data is missing

    today = date.today().isoformat()
    rows = [{"snapshot": today, "user": etoro_username, "month": k, "return": v, "risk": risk, "auc": auc} for k, v in month_returns.items()]
    return pd.DataFrame(rows)

def save_data_to_csv(df, filename="etoro_stats.csv"):
    # Check if file exists; if it does, append; otherwise, create a new one with headers
    if not df.empty:
        df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename), index=False)

def pick_consistent(df_month):
    # df_month has one row per investor with columns r_{t-11} … r_t, risk, auc
    df_month["score"] = (df_month.filter(like="r_") > 0).sum(axis=1)
    top10 = df_month.nlargest(10, ["score", "risk", "total_return"])
    winner = top10.nlargest(1, ["score", "risk", "total_return"]).iloc[0]["user"]
    return winner, set(top10["user"])

def load_month(month_end):
    # Placeholder: Load data for the given month
    # You can adapt this function to read from a file, API, or database.
    return pd.DataFrame()  # Return an empty DataFrame for now to avoid NoneType error

cash = 10_000
current = None
equity_curve = []

# Define a month sequence (e.g., last 12 months) with 'ME' instead of 'M'
month_sequence = pd.date_range(start="2025-05-01", end="2025-12-31", freq="ME").strftime('%Y-%m').tolist()

# Process each month and scrape the data for the investor
for month_end in month_sequence:
    df = load_month(month_end)
    if df is None or df.empty:
        continue  # Skip if there's no data for this month
    
    # Scrape the data for each user (in this case, just an example username)
    etoro_username = "sample_username"  # Replace with the actual username
    stats_df = grab_stats(etoro_username)
    save_data_to_csv(stats_df)  # Save the stats to CSV

    new_winner, top10 = pick_consistent(df)

    # Switch logic based on top 10 investors
    if current not in top10:
        current = new_winner  # Close old, open new
        cash *= (1 - 0.001)   # 0.1% switch friction

    # Apply performance of current investor this month
    mret = df[df.user == current][f"r_{month_end}"].values[0]
    cash *= (1 + mret)
    equity_curve.append({"date": month_end, "value": cash})

# Optionally, convert equity_curve to a DataFrame for further analysis
equity_df = pd.DataFrame(equity_curve)
print(equity_df)

# Save the equity curve to CSV if needed
equity_df.to_csv("equity_curve.csv", index=False)
