import streamlit as st
import requests
import random

def fetch_images(query):
    search_url = f"https://lexica.art/api/v1/search?q={query}"
    response = requests.get(search_url)

    if response.status_code == 200:
        data = response.json()
        images = data['images']
        
        
        
        i = 0
        img_urls = []
        while len(img_urls) < 20:
            if images[i]['nsfw'] == False:
                img_urls.append(images[i]['srcSmall'])
            i += 1
        
        random_images = random.sample(img_urls, min(6, len(img_urls)))

        #print(img_urls)
        return random_images
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
        cols = st.columns(3)
        
        for i, img_url in enumerate(images):
            cols[i % 3].image(img_url)
    else:
        st.write("No images found.")

        