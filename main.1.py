import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

hdfc_data = yf.download("HDFCBANK.NS", start = '2013-01-01', end = '2024-12-11')
icici_data = yf.download("ICICIBANK.NS", start = '2013-01-01', end = '2024-12-11')
hdfc_df = hdfc_data[["Close"]].rename(columns={"Close": "hdfc bank Close"})
icici_df = icici_data[["Close"]].rename(columns={"Close": "icici bank Close"})

combined_df = pd.merge(hdfc_df, icici_df, left_index=True, right_index=True)
plt.figure(figsize=(12, 6))
plt.plot(combined_df.index, combined_df["hdfc bank Close"], label= "HDFC BANK", color= "blue")
plt.plot(combined_df.index, combined_df["icici bank Close"], label = "ICICI BANK", color = "green")

plt.title("HDFC BANK VS ICICI BANK(2013-2024)")
plt.xlabel("Date")
plt.ylabel("Close")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()