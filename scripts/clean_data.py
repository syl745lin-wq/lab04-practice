import pandas as pd

raw_df = pd.read_csv("data/raw_transactions.csv")

print("Missing values in raw data:")
print(raw_df.isna().sum())

clean_df = raw_df.dropna(subset=["Store_ID"]).copy()

print("Rows before:", len(raw_df))
print("Rows after dropping missing Store_ID:", len(clean_df))
group_medians = clean_df.groupby("Units_Sold")["Revenue"].transform("median")
clean_df["Revenue"] = clean_df["Revenue"].fillna(group_medians)
clean_df["Revenue"] = clean_df["Revenue"].fillna(clean_df["Revenue"].median())

print("Missing values after cleaning:")
print(clean_df.isna().sum())

clean_df.to_csv("data/clean_transactions.csv", index=False)