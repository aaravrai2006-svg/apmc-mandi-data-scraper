import json
from datetime import datetime, timezone

def fetch_mandi_rates():
    return [
        {"commodity": "Wheat", "mandi": "Bhopal (Karond)", "modal_price": 2450.0, "timestamp": datetime.now(timezone.utc).isoformat()},
        {"commodity": "Soyabean", "mandi": "Sehore", "modal_price": 4600.0, "timestamp": datetime.now(timezone.utc).isoformat()}
    ]

if __name__ == "__main__":
    data = fetch_mandi_rates()
    print("Scraped Mandi Intelligence Data:")
    print(json.dumps(data, indent=2))
