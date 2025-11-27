import pandas as pd
import clickhouse_connect

client = clickhouse_connect.get_client(
    host="localhost", port=8123, username="default", password=""
)
df_clean = pd.read_parquet("clean/oecd_clean.parquet")
client.insert_df("oecd_curated", df_clean)
