import requests
import json

# सही URL डालो
profiles_url = "http://msmpr.free.nf/profiles.json"
reels_url = "http://msmpr.free.nf/reels.json"

# Headers ताकि वेबसाइट JSON भेजे
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "http://msmpr.free.nf/",
}

try:
    # JSON डेटा डाउनलोड करो
    profiles_data = requests.get(profiles_url, headers=headers).json()
    reels_data = requests.get(reels_url, headers=headers).json()

    # profiles.json सेव करो
    with open("profiles.json", "w", encoding="utf-8") as f:
        json.dump(profiles_data, f, indent=4)

    # reels.json सेव करो
    with open("reels.json", "w", encoding="utf-8") as f:
        json.dump(reels_data, f, indent=4)

    print("✅ JSON फाइलें अपडेट हो गईं!")

except Exception as e:
    print(f"⚠️ Error: {e}")
