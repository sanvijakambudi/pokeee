import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="YC News Scraper", page_icon="📰")

st.title("📰 Y Combinator News Headlines Scraper")
st.write("This app scrapes latest headlines from Hacker News (Y Combinator).")

url = "https://news.ycombinator.com/"

if st.button("Fetch Headlines"):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        headlines = soup.find_all("span", class_="titleline")

        if not headlines:
            st.warning("No headlines found. The page structure may have changed.")
        else:
            st.subheader("Top Headlines")
            for i, headline in enumerate(headlines, 1):
                text = headline.get_text()
                link = headline.find("a")

                if link and link.get("href"):
                    st.markdown(f"{i}. [{text}]({link['href']})")
                else:
                    st.write(f"{i}. {text}")

    except requests.exceptions.RequestException as e:
        st.error(f"Network error: {e}")
    except Exception as e:
        st.error(f"Something went wrong: {e}")

st.markdown("---")
st.caption("Built using Streamlit + BeautifulSoup")
