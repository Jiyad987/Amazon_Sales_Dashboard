import streamlit as st
import pandas as pd
import openai
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Function to load data
def load_data():
    file_path = "Amazon_Data.xlsx"
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}")
        return None
    
    try:
        # Try reading as Excel
        return pd.read_excel(file_path,engine='openpyxl')
    except Exception as e:
        st.error(f"Error reading Excel file: {e}")
        return None
        # return pd.read_csv(file_path)

# Function to generate response from OpenAI
def get_openai_response(prompt, data_context):
    try:
        client = openai.OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=st.secrets["openrouter"]["api_key"]  # Updated to match TOML structure
        )
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo-0613", 
            messages=[
                {"role": "system", "content": f"You are a helpful assistant that provides information about products based on this data: {data_context}. Respond concisely and accurately."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error getting response: {str(e)}"

# Load the data 
df = load_data()
if df is None:
    st.error("Failed to load data. Please check if the data file exists.")
    st.stop()
# Create a data context string
data_context = df.head(30).to_string()

# App title
st.title("Product Data Assistant")

# Create a container for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask about product data..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Get specific information from dataframe based on query
            response = get_openai_response(prompt, data_context)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display dataframe in expander for debugging/development
with st.expander("View Dataset", expanded=False):
    st.dataframe(df)

# Sidebar with info
with st.sidebar:
    st.header("About")
    st.write("This chatbot answers questions about product data")
    st.write("You can ask questions like:")
    st.write("- What are the most expensive products?")
    st.write("- How many items shipped to Bangladesh in June?")
    st.write("- Which product has the most reviews?")