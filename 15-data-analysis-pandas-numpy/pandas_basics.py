"""Pandas: DataFrames for tabular data - filtering, grouping, and merging."""

import pandas as pd

df = pd.read_csv("sample_sales.csv")
print(df.head())
print(df.dtypes)

# Filtering
nairobi_sales = df[df["region"] == "Nairobi"]
print(nairobi_sales)

# New computed column
df["revenue"] = df["units"] * df["unit_price"]
print(df[["date", "product", "revenue"]])

# groupby + aggregation - total revenue per region
revenue_by_region = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
print(revenue_by_region)

# groupby with multiple aggregations
summary = df.groupby("product").agg(
    total_units=("units", "sum"),
    avg_price=("unit_price", "mean"),
    orders=("units", "count"),
)
print(summary)

# Merging two DataFrames - a common real-world need
regions = pd.DataFrame({
    "region": ["Nairobi", "Mombasa", "Kisumu"],
    "population_millions": [4.4, 1.2, 0.6],
})
merged = df.merge(regions, on="region", how="left")
print(merged[["region", "revenue", "population_millions"]].head())
