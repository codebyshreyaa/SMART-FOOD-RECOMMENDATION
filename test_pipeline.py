import pandas as pd
import numpy as np

def precision_at_k(recommended, actual, k=5):
    if len(actual) == 0:
        return 0
    recommended = recommended[:k]
    hits = len(set(recommended) & set(actual))
    return hits / k

def recall_at_k(recommended, actual, k=5):
    if len(actual) == 0:
        return 0
    recommended = recommended[:k]
    hits = len(set(recommended) & set(actual))
    return hits / len(actual)

def run_tests():
    interactions = pd.read_csv("data/interactions.csv", parse_dates=["timestamp"])
    items = pd.read_csv("data/items.csv")

    interactions = interactions.sort_values("timestamp")
    n = len(interactions)
    train_end = int(0.7 * n)
    val_end = int(0.85 * n)

    train = interactions.iloc[:train_end]
    val = interactions.iloc[train_end:val_end]
    test = interactions.iloc[val_end:]

    # Popularity-based recommender
    popularity = train["item_id"].value_counts().reset_index()
    popularity.columns = ["item_id", "score"]

    test_users = test["user_id"].unique()
    precision_list = []
    recall_list = []

    for user in test_users:
        actual_items = test[test["user_id"] == user]["item_id"].tolist()
        recommended_items = popularity["item_id"].tolist()[:10]
        p = precision_at_k(recommended_items, actual_items, k=5)
        r = recall_at_k(recommended_items, actual_items, k=5)
        precision_list.append(p)
        recall_list.append(r)

    print("✅ Test Results (Baseline Popularity Model)")
    print(f"Precision@5: {np.mean(precision_list):.3f}")
    print(f"Recall@5:    {np.mean(recall_list):.3f}")

if __name__ == "__main__":
    run_tests()
