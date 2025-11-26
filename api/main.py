from fastapi import FastAPI
from clickhouse_connect import Client

app = FastAPI()
client = Client(host="clickhouse", port=8123)


def query_oecd():
    result = client.query_df("SELECT * FROM oecd_curated LIMIT 100")
    return result.to_dict(orient="records")
