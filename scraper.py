import json
import requests
from bs4 import BeautifulSoup

URL = "https://example.com"

response = requests.get(URL, timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

results = []

for link in soup.find_all("a"):
    text = link.get_text(strip=True)
    href = link.get("href")

    if text and href:
        results.append({
            "title": text,
            "url": href
        })

with open("results.json", "w") as file:
    json.dump(results, file, indent=2)

print(f"Saved {len(results)} results.")
