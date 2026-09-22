import pandas as pd
import numpy as np

np.random.seed(42)
data = {
    'Transaction_ID': range(1001, 1101),
    'Store_ID': np.random.choice(['Store_A', 'Store_B', 'Store_C', None], 100, p=[0.4, 0.3, 0.2, 0.1]),
    'Revenue': np.random.choice([50, 120, 250, 500, np.nan], 100, p=[0.3, 0.4, 0.15, 0.10, 0.05]),
    'Units_Sold': np.random.randint(1, 12, size=100)
}
df = pd.DataFrame(data)
df.to_csv("data/raw_transactions.csv", index=False)