#imports
import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
import requests


#Intro
st.set_page_config(page_title="Petite te pone a pensar",
                   page_icon="📖",
                   layout="centered")

# Custom CSS to style the text size and background color
st.markdown("""
    <style>
    .box-style {
        font-family: 'Arial', sans-serif;
        font-size: 18px;
        background-color: #fdecce;
        text-align: center;
        border-radius: 5px;
    }
    .pink-style {
        background-color: #ffd6e5;
        border-radius: 10px;
        padding: 15px;
    }
    .light-blue-style {
        font-family: 'Sans-serif', Arial, Helvetica, sans-serif;
        font-size: 36px;
        font-weight: bold;
        background-color: #d6ecff;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        
    }
    .quote-container {
        background-color: #f0f8ff;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 18px;
        color: #333;
    }
    
    /* Style for the primary button */
    /* Hover effect for the primary button */
    button[kind="primary"]:hover {
        background-color: white;  /* White background */
        color: #d3a7e3;  /* Light purple text */
        border: 2px solid #d3a7e3;
    }
    button[kind="primary"] {
        background-color: #d3a7e3;  /* Light purple color */
        color: white;
        border: 2px solid white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        text-align: center;
    }


    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='light-blue-style'> 📖<br> Petite te pone a pensar </div>", unsafe_allow_html=True)
st.divider()

col1,col2= st.columns(2,gap='medium',border=True)

with col1:
        st.image("./images/inicio.jpg",width=250,use_container_width=True)


with col2:
    st.markdown(
        f"<div class='quote-container'> <br>English switch! you need to be prepared for when you come to greece with me 💃💃 ;) (because neither you or me can speech greek yet..)."
        f" <br>So to get start it feel enlight it with some quotes to make you think as those great greek philosophers 💭 and why not? some random facts valen 🤪 loves to share with you...</div>",
        unsafe_allow_html=True)
    st.markdown('')
    if st.button("Quote of the day!", use_container_width=True, type='primary'):
        st.session_state.quote = 'nada'

st.markdown('')
def fetch_quote():
    url = "https://api.quotable.io/random"
    try:
        response = requests.get(url, verify=False)  # Desactivar verificación SSL
        response.raise_for_status()  # Verifica errores HTTP
        data = response.json()
        return f"'{data['content']}' — {data['author']}"
    except requests.exceptions.RequestException:
        return "Ups, no se pudo obtener una frase. Inténtalo de nuevo más tarde."

# create the quote
#quote = fetch_quotes()


with st.container():
    # Display the motivational quote
    if "quote" not in st.session_state or st.session_state.quote is 'nada':
        st.session_state.quote = fetch_quote()
        st.markdown(f"<div class='quote-container'>{st.session_state.quote}</div>", unsafe_allow_html=True)


