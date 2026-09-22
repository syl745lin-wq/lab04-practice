import pandas as pd

raw_df = pd.read_csv("data/raw_transactions.csv")

print("Missing values in raw data:")
print(raw_df.isna().sum())

clean_df = raw_df.dropna(subset=["Store_ID"]).copy()

print("Rows before:", len(raw_df))
print("Rows after dropping missing Store_ID:", len(clean_df))