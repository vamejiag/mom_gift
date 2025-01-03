#imports
import streamlit as st
import requests
from datetime import datetime
import random
from apify_client import ApifyClient # for images scrapper
import random
import numpy as np
import pandas as pd
from pathlib import Path

#Intro
st.set_page_config(page_title="Por qué te amo?",
                   page_icon="❤️")

st.markdown("# ❤️ Por qué te amo?")
# Custom CSS for styling
st.markdown("""
    <style>
    .snoopy-image-container {
        text-align: center;
        background-color: #f0f8ff;
        border-radius: 10px;
        padding: 10px;
    }
    .reason-container {
        background-color: #f0f8ff;
        border:2px solid #d5f0f2;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 18px;
        font-weight: bold;
        color: #333;
    }
    .day-container {
        background-color: #f0f8ff;
        border:2px solid #d5f0f2;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 20px;
    }
    
    .text-container {
        background-color: #ffe8f8;
        border-radius: 10px;
        border:2px solid #e6bad9;
        padding: 20px;
        text-align: center;
        font-size: 23px;
        font-weight: lighter;
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
    </style>
""", unsafe_allow_html=True)

st.info('necesito explicarlo? no creo peeero siempre es bueno recordarle a mi quinceañera cuanto la amo y cuanto extraño'
        ' esas salidas a Olivia, esas cantadas a pulmon con Morat, esos secretos guardados, las cantaletas y los noches de chismes jugosos en la cocina')
st.divider()

# Snoopy Image Fetcher
def fetch_random_snoopy_image():
    data_set = './images_snoopy.xlsx'
    df = pd.read_excel(data_set)
    id = np.random.randint(0,365,1)[0]
    url = df[df['id']==id]['imageUrl'].item()

    return str(url)


# List of reasons why you love your mom
df = pd.read_csv("razones_mom.txt",delimiter=';',header=0)
reasons = df[' output'].to_list()


# Generate a reason per day
current_day = datetime.now().day
reason_for_today = reasons[current_day % len(reasons)]

# Layout: Two columns
col1, col2 = st.columns(2, gap='large')

# Column 1: Display a random Snoopy image
with col1:
    image_url = fetch_random_snoopy_image()
    try:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src={image_url} alt="Snoopy Image" style="width:300px; 
                border:2px solid lightgray; border-radius:10px;">
                <p style="font-size: 16px; color: gray;"></p>
            </div>
            """,
            unsafe_allow_html=True
        )
    except Exception as e:
        image_url = "https://i.pinimg.com/736x/ef/33/18/ef331898ef87f80ce6c96ef049ba983f.jpg"
        st.markdown(
            f"""
                    <div style="text-align: center;">
                        <img src={image_url} alt="Snoopy Image" style="width:300px; 
                        border:2px solid lightgray; border-radius:10px;">
                        <p style="font-size: 16px; color: gray;">Random Snoopy Image</p>
                    </div>
                    """,
            unsafe_allow_html=True
        )
    st.markdown("<div class='snoopy-image-container'>Enjoy Snoopy's fun vibes! 🐾</div>", unsafe_allow_html=True)

# Column 2: Display the reason and date
with col2:
    st.markdown("<div class='reason-container'>Why I Love My Mom Today</div>", unsafe_allow_html=True)
    st.markdown("\n\n")
    st.markdown(
        f"<div class='day-container'>{datetime.now().strftime('%B %d, %Y')}<br></div>",
        unsafe_allow_html=True
    )
    st.markdown("\n\n")
    st.markdown(f"<div class='text-container'>.......🎀........<br>{reason_for_today}</div>",
        unsafe_allow_html=True
    )

