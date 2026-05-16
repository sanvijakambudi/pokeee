import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("span", class_="titleline")

print("\nTop Headlines:\n")

for i, headline in enumerate(headlines, 1):
    print(i, "-", headline.text)