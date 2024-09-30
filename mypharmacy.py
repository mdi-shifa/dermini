import pandas as pd
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def search_medicine_skincare(medicine_name):
    # Simulated data for skincare products
    data = {
        "Product Name": ["Amoxicillin Cream", "Benzoyl Peroxide Gel", "Salicylic Acid Solution", "Deriva BPO Gel", "Dermadew Acne Soap", "Photoban Aqua Gel", "Fewnex Tablet"],
        "Link": [
            "https://www.skincarepharmacy.com/shop/amoxicillin-cream",
            "https://www.skincarepharmacy.com/shop/benzoyl-peroxide-gel",
            "https://www.skincarepharmacy.com/shop/salicylic-acid-solution",
            "https://www.skincarepharmacy.com/shop/deriva-bpo-gel",
            "https://www.skincarepharmacy.com/shop/dermadew-acne-soap",
            "https://www.skincarepharmacy.com/shop/photoban-aqua-gel",
            "https://www.skincarepharmacy.com/shop/fewnex-tablet"
        ],
        "Price": [200, 150, 300, 250, 120, 400, 90]
    }

    # Convert the data to a pandas DataFrame for easier manipulation and display
    df = pd.DataFrame(data)
    
    # Use fuzzy matching to find the best match for the medicine name
    product_names = df['Product Name'].tolist()
    best_match, score = process.extractOne(medicine_name, product_names, scorer=fuzz.token_sort_ratio)
    
    # Set a threshold for matching (e.g., 70% similarity or higher)
    if score >= 70:
        # Return the row that matches the best match
        filtered_df = df[df['Product Name'] == best_match]
    else:
        filtered_df = pd.DataFrame()  # Return empty DataFrame if no match is found

    return filtered_df
