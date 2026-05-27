import pandas as pd

def load_data():
    inventory = pd.DataFrame({
        "Product_Name": ["milk", "bread", "egg"]
    })

    recipes = pd.DataFrame({
        "name": ["toast", "omelette"],
        "ingredients": [
            "bread,milk",
            "egg,milk"
        ]
    })

    return inventory, recipes
