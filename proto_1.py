import streamlit as st
import requests

def fetch_images(query):
    search_url = f"https://lexica.art/api/v1/search?q={query}"
    response = requests.get(search_url)

    if response.status_code == 200:
        data = response.json()
        images = data['images']
        
        # Grab the first 4 images
        img_urls = [images[i]['srcSmall'] for i in range(min(4, len(images)))]
        return img_urls
    else:
        return []

# Streamlit app
st.title("Moodboard from Lexica.art")
query = st.text_input("Enter search query:")

if query:
    st.write(f"Searching for: {query}")
    images = fetch_images(query)
    
    if images:
        # Create a 2x2 grid using columns
        cols = st.columns(2)
        
        for i, img_url in enumerate(images):
            cols[i % 2].image(img_url)
    else:
        st.write("No images found.")