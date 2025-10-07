import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

def generate_datasets(output_dir="data"):
    os.makedirs(output_dir, exist_ok=True)
    
    random.seed(42)
    np.random.seed(42)

    # ---------- ITEMS ----------
    cuisines = ["Indian", "Italian", "Chinese", "Mexican", "American"]
    tags = ["vegan", "gluten-free", "spicy", "sweet", "low-calorie", "protein-rich"]

    items = []
    for i in range(1, 1001):
        cuisine = random.choice(cuisines)
        calories = random.randint(100, 800)
        item_tags = ",".join(random.sample(tags, k=random.randint(1, 3)))
        items.append([
            i,
            f"Food Item {i}",
            cuisine,
            calories,
            random.randint(5, 50),
            random.randint(10, 100),
            random.randint(1, 30),
            item_tags
        ])
    
    items_df = pd.DataFrame(items, columns=["item_id", "name", "cuisine", "calories", "protein", "carbs", "fat", "tags"])
    items_df.to_csv(f"{output_dir}/items.csv", index=False)

    # ---------- USERS ----------
    users = []
    for u in range(1, 201):
        users.append([
            u,
            random.randint(18, 60),
            random.choice(["male", "female"]),
            random.choice(["vegan", "non-veg", "vegetarian", "gluten-free"]),
            random.choice(["India", "USA", "UK", "Canada"])
        ])
    users_df = pd.DataFrame(users, columns=["user_id", "age", "gender", "diet_type", "location"])
    users_df.to_csv(f"{output_dir}/users.csv", index=False)

    # ---------- INTERACTIONS ----------
    interactions = []
    start_date = datetime(2024, 1, 1)
    for _ in range(10000):
        user = random.randint(1, 200)
        item = random.randint(1, 1000)
        rating = random.randint(1, 5)
        timestamp = start_date + timedelta(days=random.randint(0, 365))
        interactions.append([user, item, rating, timestamp])

    interactions_df = pd.DataFrame(interactions, columns=["user_id", "item_id", "rating", "timestamp"])
    interactions_df.to_csv(f"{output_dir}/interactions.csv", index=False)

    print(f"✅ Dataset generated in '{output_dir}'")

if __name__ == "__main__":
    generate_datasets()
