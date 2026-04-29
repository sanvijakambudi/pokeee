import requests
import json

movie_name = "Fight Club"
API = "AIzaSyCDzYk2Kcliz7asmkoFZjERmwUaW1XPOtk"
response = requests.get(f"http://www.omdbapi.com/?t={movie_name}&apikey={API}")
data = json.loads(response.text)

if data["Response"] == "True":
    print("Title:", data["Title"])
    print("Year:", data["Year"])
    print("Rating:", data["imdbRating"])
else:
    print("Movie not found")
    