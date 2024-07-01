import streamlit as st
import requests
from bs4 import BeautifulSoup
from pprint import pprint

def fetch_images(query):
    search_url = f"https://lexica.art/api/v1/search?q={query}"
    response = requests.get(search_url)

    print(response.status_code)
    data = response.json()
    images = data['images']
    
    # grap 5 first images
    img_urls = []
    for i in range(5):
        img_urls.append(images[i]['srcSmall'])

    return img_urls


# Streamlit app
st.title("Image Search from Lexica.art")
query = st.text_input("Enter search query:")

if query:
    st.write(f"Searching for: {query}")
    images = fetch_images(query)
    
    if images:
        for img_url in images:
            st.image(img_url)
    else:
        st.write("No images found.")
    
    
    