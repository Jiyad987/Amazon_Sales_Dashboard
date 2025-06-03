import streamlit as st

st.write("Amazon Sales Dashboard")
st.sidebar.title("Amazon Sales Dashboard")

p1 = st.Page("pages/dashboard.py", title="Dashboard", icon="📊")
p2 = st.Page("pages/ai_chat.py", title="AI Chatbot", icon="🤖")
p3 = st.Page("pages/product_catlog.py", title="Product Catalog", icon="📦")

pg = st.navigation({
    "Amazon Sales Dashboard": [p1, p2, p3]
})
pg.run()