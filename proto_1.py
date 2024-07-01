import streamlit as st
import requests
from bs4 import BeautifulSoup

def fetch_images(query):
    search_url = f"https://lexica.art/?q={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Use the correct class name identified in the HTML inspection
    image_tags = soup.find_all("img", class_="pointer-events-none")  # class from lexica.art 
    return image_urls


# Streamlit app
st.title("Image Search from Lexica.art")ß
query = st.text_input("Enter search query:")

if query:
    st.write(f"Searching for: {query}")
    images = fetch_images(query)
    
    if images:
        for img_url in images:
            st.image(img_url)
    else:
        st.write("No images found.")
    
    
    