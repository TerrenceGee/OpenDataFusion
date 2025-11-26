import requests
from utils.storage import save_to_raw

data = requests.get("https://example.oecd.api").json()
save_to_raw(data, "oecd_raw.json")
