from fastapi import FastAPI
from clickhouse_connect import get_client

app = FastAPI()
client = get_client(host="clickhouse", port=8123)


@app.get("/oecd")
def query_oecd():
    result = client.query_df("SELECT * FROM oecd_curated LIMIT 100")
    return result.to_dict(orient="records")
