import streamlit as st

# Mock data for products on famous online stores
product_data = {
    "nykaa": [
        {"name": "Cetaphil Gentle Skin Cleanser", "price": "500", "link": "https://www.nykaa.com/cetaphil-gentle-cleanser"},
        {"name": "The Face Shop Rice Water Bright Foaming Cleanser", "price": "650", "link": "https://www.nykaa.com/face-shop-cleanser"},
        {"name": "Explore more brands", "link": "https://www.nykaa.com/skincare"}
    ],
    "amazon": [
        {"name": "Neutrogena Hydro Boost Water Gel", "price": "850", "link": "https://www.amazon.in/neutrogena-hydro-boost"},
        {"name": "Olay Regenerist Micro-Sculpting Cream", "price": "1250", "link": "https://www.amazon.in/olay-regenerist-cream"},
        {"name": "Explore more brands", "link": "https://www.amazon.in/s?k=skincare"}
    ],
}

# Function to search products by brand or product name
def search_product(brand_or_product):
    results = []
    for store, products in product_data.items():
        for product in products:
            if brand_or_product.lower() in product["name"].lower():
                results.append({"store": store, "product": product})
    if not results:  # If no specific product is found, return the general store link
        for store, products in product_data.items():
            results.append({
                "store": store, 
                "product": {"name": f"Explore more {store.title()} brands", "price": "", "link": products[-1]["link"]}
            })
    return results

# Function to handle skincare-related questions
def skincare_question_answer(question):
    # Sample answers for common skincare questions
    answers = {
        "korean skincare": """
        **Korean skincare** emphasizes hydration and gentle formulas, often involving multiple steps. 
        **Pros:** Great for hydration and skin barrier repair. 
        **Cons:** Some routines can be time-consuming and expensive.
        """,
        "anti-aging": """
        **Anti-aging products** help reduce the appearance of wrinkles and fine lines. Key ingredients to look for are Retinol, Vitamin C, and Hyaluronic Acid.
        **Pros:** Helps improve skin texture and elasticity. 
        **Cons:** Can cause irritation if overused.
        """,
        "sunscreen": """
        **Sunscreen** is vital for protecting against UV rays. Use a broad-spectrum SPF of 30 or higher.
        **Pros:** Prevents skin damage and reduces the risk of skin cancer. 
        **Cons:** Needs regular reapplication for effectiveness.
        """,
    }

    fallback_response = """
    I'm still learning, but here are some skincare tips:
    1. Always cleanse your face gently.
    2. Moisturize daily to keep your skin hydrated.
    3. Apply sunscreen every day, even when it's cloudy!

    For detailed queries, please ask about specific products or skincare concerns like acne or dry skin.
    """

    for key in answers:
        if key in question.lower():
            return answers[key]
    
    return fallback_response

# Function to display the shop page
def shop():
    st.title("Shop Skincare & Query Assistant 🛍️💬")

    # Tabbed layout
    tab1, tab2 = st.tabs(["🛍️ Shop Skincare", "💬 Skincare Queries"])

    # Tab 1: Skincare Shop
    with tab1:
        st.header("Skincare and Cosmetic Shop")
        st.write("Search for skincare and cosmetic products from popular online stores like Nykaa and Amazon.")
        
        # Product search input
        search_query = st.text_input("Enter a skincare brand or product name:")
        if st.button("Search Products"):
            if search_query:
                search_results = search_product(search_query)
                if search_results:
                    st.success("Products found!")
                    st.balloons()
                    for result in search_results:
                        product = result["product"]
                        store = result["store"]
                        if product["price"]:  # If price is available, show it
                            st.markdown(f"**{product['name']}** - {product['price']} ₹ [Buy Here]({product['link']})")
                        else:  # If no specific product found, show general store link
                            st.markdown(f"**{product['name']}** - [Explore on {store.title()}]({product['link']})")
                else:
                    st.error("No products found. Try another search.")
            else:
                st.error("Please enter a search query.")

    # Tab 2: Skincare Questions
    with tab2:
        st.header("Skincare Queries Assistant")
        st.write("Ask me anything about skincare products, routines, or concerns!")

        # Input for skincare question
        user_question = st.text_input("Enter your skincare question:")
        if st.button("Get Answer"):
            if user_question:
                answer = skincare_question_answer(user_question)
                st.markdown(answer)
            else:
                st.error("Please enter a question.")

if __name__ == "__main__":
    shop()
