import requests

API_URL = "https://api.openaq.org/v2/measurements?city=Paris&limit=5"
LOCAL_API_URL = "http://127.0.0.1:8000/air_quality/"

def fetch_openaq():
    response = requests.get(API_URL)
    data = response.json()
    results = data.get("results", [])
    for item in results:
        payload = {
            "city": item.get("city", "Paris"),
            "location": item.get("location", ""),
            "parameter": item.get("parameter", ""),
            "value": item.get("value", 0),
            "unit": item.get("unit", ""),
            "date_utc": item.get("date", {}).get("utc", "")
        }
        r = requests.post(LOCAL_API_URL, json=payload)
        print(f"Status: {r.status_code}, Data: {r.json()}")

if __name__ == "__main__":
    fetch_openaq()
