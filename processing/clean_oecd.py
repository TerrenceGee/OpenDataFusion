import pandas as pd

df = pd.read_json("raw/oecd_raw.json")

df_clean = df.dropna()
df_clean.to_parquet("clean/oecd_clean.parquet")
