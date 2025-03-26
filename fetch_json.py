import requests
import json

# Proxy URL (इसे बदल सकते हैं)
proxy_url = "https://api.allorigins.win/get?url="

# Original URLs
url1 = "http://msmpr.free.nf/profiles.json"
url2 = "http://msmpr.free.nf/reels.json"

# Headers सेट करें ताकि सर्वर इसे ब्राउज़र रिक्वेस्ट समझे
headers = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_json(proxy, url):
    try:
        response = requests.get(proxy + url, headers=headers, timeout=10)
        if response.status_code == 200:
            return json.loads(response.json()["contents"])  # JSON कंटेंट निकालें
        else:
            return {}
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return {}

# JSON डेटा लोड करें
data1 = fetch_json(proxy_url, url1)
data2 = fetch_json(proxy_url, url2)

# JSON फाइल सेव करें
with open("profiles.json", "w") as f1:
    json.dump(data1, f1)

with open("reels.json", "w") as f2:
    json.dump(data2, f2)
