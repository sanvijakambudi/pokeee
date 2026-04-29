import streamlit as st
import pandas as pd

st.title("Pokedex")

pokedex_df = pd.read_csv("pokedex.csv")
st.write(pokedex_df)