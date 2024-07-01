import streamlit as st

# Set the title of the web app
st.title("Embedded Lexica.art Search")

# Input text box for the search query
query = st.text_input("Search on Lexica.art:")

# If the query is not empty, update the iframe URL
if query:
    lexica_url = f"https://lexica.art/?q={query}"
else:
    lexica_url = "https://lexica.art"

# Embed the Lexica.art website using an iframe
st.markdown(
    f'<iframe src="{lexica_url}" width="100%" height="600px" frameborder="0"></iframe>',
    unsafe_allow_html=True
)