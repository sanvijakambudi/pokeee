import requests
import json
import streamlit as st
from dotenv import load_dotenv
import os

if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv(override=True)
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    try:
        API_KEY = st.secrets["API_KEY"]
    except Exception:
        API_KEY = None
if not API_KEY:
    st.error("No API Key found!")
    st.stop()

st.title("MovieDex DB")

movie_name = st.text_input("Enter a movie name", "Fight Club")
response = requests.get(f"http://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}")
data = json.loads(response.text)
# st.write(data)
if(data["Response"] == "False"):
    st.error("Movie not found")
else:
    fields = ['Title', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writer', 'Actors', 'Plot', 'Language', 'Country', 'Awards', 'Metascore', 'imdbRating', 'BoxOffice']
    selected_field = st.selectbox("Select a field", fields)
    st.write(f"{selected_field} = {data[selected_field]}")
    st.image(data["Poster"])
    