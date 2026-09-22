from pathlib import Path

import pandas as pd

repo_dir = Path(__file__).resolve().parent.parent
df = pd.read_csv(repo_dir / "data" / "analyzed_transactions.csv")

store_summary = df.groupby("Store_ID").agg(
    total_revenue=("Revenue", "sum"),
    avg_units_sold=("Units_Sold", "mean"),
    unique_order_segments=("order_segment", lambda values: ", ".join(sorted(values.unique()))),
)

q1 = df["Revenue"].quantile(0.25)
q3 = df["Revenue"].quantile(0.75)
iqr = q3 - q1
median_revenue = df["Revenue"].median()

threshold = median_revenue + 1.5 * iqr
outliers = df[df["Revenue"] > threshold]

results_dir = repo_dir / "results"
results_dir.mkdir(exist_ok=True)

report = results_dir / "store_report.txt"
with report.open("w") as file:
    file.write("Store summary\n")
    file.write(store_summary.to_string())
    file.write("\n\nHigh-revenue transactions\n")
    file.write(f"Threshold: Revenue > {threshold}\n")
    file.write(outliers.to_string(index=False))

print(store_summary)
print(f"\nOutliers found: {len(outliers)}")
print(f"Report saved to: {report}")