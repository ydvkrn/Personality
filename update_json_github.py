import requests
import json

# ✅ GitHub Repository Details
GITHUB_USERNAME = "ydvkrn"  # अपना GitHub Username डालो
REPO_NAME = "Personality"  # Repository Name डालो
ACCESS_TOKEN = "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"  # अपना GitHub Token डालो

# ✅ JSON Data Links
profiles_url = "http://msmpr.free.nf/profiles.json"
reels_url = "http://msmpr.free.nf/reels.json"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Authorization": f"token {ACCESS_TOKEN}"
}

def fetch_json(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"⚠️ Error fetching {url}: {e}")
        return None

def update_github_file(file_path, new_content):
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/contents/{file_path}"
    
    # GitHub से फाइल की Details लो
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_data = response.json()
        sha = file_data["sha"]
    else:
        sha = None  # फाइल पहली बार बनानी है

    # GitHub पर JSON Push करो
    data = {
        "message": f"Updated {file_path}",
        "content": json.dumps(new_content, indent=4).encode("utf-8").decode("utf-8"),
        "branch": "main"
    }
    
    if sha:
        data["sha"] = sha

    update_response = requests.put(url, headers=headers, json=data)
    if update_response.status_code in [200, 201]:
        print(f"✅ {file_path} अपडेट हो गया!")
    else:
        print(f"⚠️ {file_path} अपडेट करने में दिक्कत: {update_response.json()}")

# ✅ JSON Data Fetch और GitHub में Update
profiles_data = fetch_json(profiles_url)
if profiles_data:
    update_github_file("profiles.json", profiles_data)

reels_data = fetch_json(reels_url)
if reels_data:
    update_github_file("reels.json", reels_data)
