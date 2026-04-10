import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
df = pd.read_csv("data/trends_analysed.csv")
# Create outputs folder
if not os.path.exists("outputs"):
    os.makedirs("outputs")
    # Top 10 stories by score
top10 = df.sort_values(by="score", ascending=False).head(10)

plt.figure()
plt.barh(top10["title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score")

plt.savefig("outputs/chart1_top_stories.png")
plt.close()
category_counts = df["category"].value_counts()

plt.figure()
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Count")
plt.title("Stories per Category")

plt.savefig("outputs/chart2_categories.png")
plt.close()
plt.figure()

popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Score vs Comments")
plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.close()
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Chart 1
axs[0, 0].barh(top10["title"], top10["score"])
axs[0, 0].set_title("Top Stories")

# Chart 2
axs[0, 1].bar(category_counts.index, category_counts.values)
axs[0, 1].set_title("Categories")

# Chart 3
axs[1, 0].scatter(popular["score"], popular["num_comments"])
axs[1, 0].set_title("Score vs Comments")

fig.suptitle("TrendPulse Dashboard")

plt.savefig("outputs/dashboard.png")
plt.close()fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Chart 1
axs[0, 0].barh(top10["title"], top10["score"])
axs[0, 0].set_title("Top Stories")

# Chart 2
axs[0, 1].bar(category_counts.index, category_counts.values)
axs[0, 1].set_title("Categories")

# Chart 3
axs[1, 0].scatter(popular["score"], popular["num_comments"])
axs[1, 0].set_title("Score vs Comments")

fig.suptitle("TrendPulse Dashboard")

plt.savefig("outputs/dashboard.png")
plt.close()