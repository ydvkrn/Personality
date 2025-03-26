import requests
import json

profiles_url = "http://msmpr.free.nf/profiles.json"
reels_url = "http://msmpr.free.nf/reels.json"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "http://msmpr.free.nf/",
}

try:
    # JSON फेच करो  
    profiles_response = requests.get(profiles_url, headers=headers)
    reels_response = requests.get(reels_url, headers=headers)

    print("🔍 Profiles Response:", profiles_response.text[:500])  
    print("🔍 Reels Response:", reels_response.text[:500])  

    # JSON में कन्वर्ट करने की कोशिश करो  
    try:
        profiles_data = profiles_response.json()
    except json.JSONDecodeError:
        print("⚠️ Profiles JSON सही नहीं है!")
        profiles_data = {}

    try:
        reels_data = reels_response.json()
    except json.JSONDecodeError:
        print("⚠️ Reels JSON सही नहीं है!")
        reels_data = {}

    # JSON फाइलें सेव करो  
    with open("profiles.json", "w", encoding="utf-8") as f:
        json.dump(profiles_data, f, indent=4)

    with open("reels.json", "w", encoding="utf-8") as f:
        json.dump(reels_data, f, indent=4)

    print("✅ JSON फाइलें अपडेट हो गईं!")

except Exception as e:
    print(f"⚠️ Error: {e}")
