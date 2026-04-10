import requests
import time
import json
import os
from datetime import datetime

TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

headers = {"User-Agent": "TrendPulse/1.0"}

categories = {
    "technology": ["ai", "software", "tech", "code", "computer"],
    "worldnews": ["war", "government", "country"],
    "sports": ["game", "team", "player"],
    "science": ["research", "study", "space"],
    "entertainment": ["movie", "music", "show"]
}

def get_category(title):
    title = title.lower()
    for cat, words in categories.items():
        for w in words:
            if w in title:
                return cat
    return None

def main():
    all_stories = []
    count = {c: 0 for c in categories}

    res = requests.get(TOP_STORIES_URL, headers=headers)
    ids = res.json()[:500]

    for i in ids:
        try:
            data = requests.get(ITEM_URL.format(i), headers=headers).json()

            if not data or "title" not in data:
                continue

            cat = get_category(data["title"])

            if cat and count[cat] < 25:
                story = {
                    "post_id": data.get("id"),
                    "title": data.get("title"),
                    "category": cat,
                    "score": data.get("score", 0),
                    "num_comments": data.get("descendants", 0),
                    "author": data.get("by"),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                all_stories.append(story)
                count[cat] += 1

            if all(v >= 25 for v in count.values()):
                break

        except:
            continue

    if not os.path.exists("data"):
        os.makedirs("data")

    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

    with open(filename, "w") as f:
        json.dump(all_stories, f, indent=4)

    print("Done! File saved:", filename)

if __name__ == "__main__":
    main()