import pandas as pd
import numpy as np
import os

os.makedirs("data", exist_ok=True)

np.random.seed(42)

categories = ["Electronics", "Clothing", "Home & Kitchen"]
subcategories = {
    "Electronics": ["Smartphones", "Laptops", "Accessories"],
    "Clothing": ["Men", "Women", "Kids"],
    "Home & Kitchen": ["Furniture", "Appliances", "Decor"]
}
regions = ["North America", "Europe", "Asia", "South America", "Africa"]

data = []

for cat in categories:
    for subcat in subcategories[cat]:
        for region in regions:
            sales = np.random.randint(5000, 30000)
            data.append([cat, subcat, region, sales])

df = pd.DataFrame(data, columns=["Category", "Subcategory", "Region", "Sales"])

df.to_csv("data/sales_hierarchy.csv", index=False)
