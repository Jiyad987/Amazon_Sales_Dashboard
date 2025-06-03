import streamlit as st

st.title("Product Catalog")

# List of available product categories
product_categories = {
    "Audio Video": "🎵",
    "Camera": "📷",
    "Car Accs": "🚗",
    "Men Clothes": "👔",
    "Laptop": "💻",
    "Men Shoes": "👞",
    "Mobile Accs": "📱",
    "Toys": "🧸"
}

# Create a container with columns for the products
cols = st.columns(4)
index = 0

# Create clickable cards for each product category
for product, icon in product_categories.items():
    col = cols[index % 4]
    with col:
        card = st.container(border=True)
        with card:
            st.markdown(f"### {icon} {product}")
            if st.button("View Details", key=product):
                # Navigate to dashboard when clicked
                st.switch_page("pages/dashboard.py")
    index += 1

# Add CSS to style the product cards
st.markdown("""
<style>
    div[data-testid="stHorizontalBlock"] > div {
        padding: 10px;
    }
    div[data-baseweb="card"] {
        margin-bottom: 20px;
        cursor: pointer;
    }
</style>
""", unsafe_allow_html=True)