import pandas as pd

def load_data():
    inventory = pd.DataFrame({
        "item": ["milk", "bread", "egg"]
    })

    recipes = pd.DataFrame({
        "recipe": ["toast", "omelette"]
    })

    return inventory, recipes
