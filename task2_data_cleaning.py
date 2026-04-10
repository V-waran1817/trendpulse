import pandas as pd
import json

# Step 1: Load JSON file
file_path = "data/trends_20260410.json"   # உன் file name change ஆகலாம்

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

print(f"Loaded {len(df)} stories from {file_path}")

# Step 2: Clean Data

# Remove duplicates
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# Remove missing values
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Convert data types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# Remove low quality (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Remove extra spaces
df["title"] = df["title"].str.strip()

# Step 3: Save as CSV
output_path = "data/trends_clean.csv"
df.to_csv(output_path, index=False)

print(f"Saved {len(df)} rows to {output_path}")

# Category summary
print("\nStories per category:")
print(df["category"].value_counts())