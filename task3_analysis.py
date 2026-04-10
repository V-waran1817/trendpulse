import pandas as pd
df = pd.read_csv("data/trends_clean.csv")
print("Loaded data:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nAverage score:", df["score"].mean())
print("Average comments:", df["num_comments"].mean())
import numpy as np
scores = df["score"]

print("\n--- NumPy Stats ---")
print("Mean score:", np.mean(scores))
print("Median score:", np.median(scores))
print("Std deviation:", np.std(scores))
print("Max score:", np.max(scores))
print("Min score:", np.min(scores))
top_category = df["category"].value_counts().idxmax()
count = df["category"].value_counts().max()

print(f"\nMost stories in: {top_category} ({count} stories)")
top_story = df.loc[df["num_comments"].idxmax()]

print(f"Most commented story: \"{top_story['title']}\" - {top_story['num_comments']} comments")
df["engagement"] = df["num_comments"] / (df["score"] + 1)

avg_score = df["score"].mean()
df["is_popular"] = df["score"] > avg_score
df.to_csv("data/trends_analysed.csv", index=False)

print("\nSaved to data/trends_analysed.csv")