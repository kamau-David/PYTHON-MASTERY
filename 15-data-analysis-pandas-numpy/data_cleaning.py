"""Common data cleaning steps: missing values, duplicates, type fixes."""

import pandas as pd
import numpy as np

df = pd.read_csv("sample_sales.csv")

print("missing values per column:")
print(df.isna().sum())

# Filling missing values - different strategies for different columns
df["units"] = df["units"].fillna(df["units"].median())
df["unit_price"] = df.groupby("product")["unit_price"].transform(
    lambda s: s.fillna(s.median())
)
print("\nafter filling missing values:")
print(df)

# Finding and dropping exact duplicate rows
print("\nduplicate rows:", df.duplicated().sum())
df_deduped = df.drop_duplicates()
print("rows before:", len(df), "rows after dedup:", len(df_deduped))

# Type conversion - date column comes in as a string by default
df["date"] = pd.to_datetime(df["date"])
print("\ndate column dtype:", df["date"].dtype)

# Deriving a new feature from the cleaned data
df["revenue"] = df["units"] * df["unit_price"]
daily_revenue = df.groupby(df["date"].dt.date)["revenue"].sum()
print("\ndaily revenue:")
print(daily_revenue)
