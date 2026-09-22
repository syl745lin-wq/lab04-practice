from pathlib import Path

import numpy as np
import pandas as pd

repo_dir = Path(__file__).resolve().parent.parent
data_dir = repo_dir / "data"

df = pd.read_csv(data_dir / "clean_transactions.csv")

df["unit_price"] = df["Revenue"] / df["Units_Sold"]

conditions = [
    (df["Revenue"] >= 300) & (df["Units_Sold"] >= 5),
    df["Revenue"] >= 100,
    df["Revenue"] < 100,
]
choices = ["Bulk High-Value", "Standard Retail", "Low-Margin"]

df["order_segment"] = np.select(conditions, choices, default="Other")

print(df.head())
print(df["order_segment"].value_counts())

df.to_csv(data_dir / "analyzed_transactions.csv", index=False)