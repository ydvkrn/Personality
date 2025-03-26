import requests
import os
import subprocess

# Fetch JSON files from InfinityFree
urls = {
    "reels.json": "http://msmpr.free.nf/reels.json",
    "profiles.json": "http://msmpr.free.nf/profiles.json"
}

for file_name, url in urls.items():
    response = requests.get(url)
    with open(file_name, "w") as f:
        f.write(response.text)

# Git commands to commit and push
subprocess.run(["git", "add", "reels.json", "profiles.json"])
subprocess.run(["git", "commit", "-m", "Auto-update JSON files from InfinityFree"])
subprocess.run(["git", "push", "origin", "main"])
