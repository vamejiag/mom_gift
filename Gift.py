import streamlit as st
import random
from transformers import pipeline


# Function to initialize the chatbot for generating 365 reasons
def generate_reasons_for_mom():
    reasons = [
        "Te amo porque me has dado siempre tu amor incondicional.",
        "Te amo porque siempre sabes cómo hacerme sentir mejor.",
        "Te amo porque eres una fuente constante de apoyo y fuerza.",
        "Te amo porque compartimos recuerdos maravillosos juntos.",
        "Te amo porque siempre sabes lo que necesito sin que te lo diga.",
        # Add more personalized reasons...
    ]
    return random.choice(reasons)


# Mood-based Song Generator
def get_song_by_mood(mood):
    mood_song_dict = {
        'happy': ['Happy Song 1', 'Happy Song 2', 'Happy Song 3'],
        'sad': ['Sad Song 1', 'Sad Song 2', 'Sad Song 3'],
        'motivated': ['Motivated Song 1', 'Motivated Song 2', 'Motivated Song 3'],
        'relaxed': ['Relaxing Song 1', 'Relaxing Song 2', 'Relaxing Song 3']
    }
    return random.choice(mood_song_dict.get(mood, []))


# Random quote generator
def get_random_quote():
    quotes = [
        "La vida es lo que pasa mientras estás ocupado haciendo otros planes. - John Lennon",
        "El amor de una madre es el combustible que permite a un ser humano hacer lo imposible. - Marion C. Garretty",
        "Dios es nuestra fortaleza y refugio, nuestra ayuda siempre presente en tiempos de angustia. - Salmo 46:1",
        "El futuro pertenece a aquellos que creen en la belleza de sus sueños. - Eleanor Roosevelt",
        # More quotes can be added
    ]
    return random.choice(quotes)


# Streamlit UI
def main():
    st.set_page_config(page_title="Para mi Snoopy",
                       page_icon="❤️",
                       layout='wide',
                       initial_sidebar_state="collapsed")

    # seting parameters
    # Example of markdown with custom font and size
    st.markdown("""
        <style>
        .custom_font {
            font-family: 'Arial', sans-serif;
            font-size: 15px;
        }
        .text {
        font-size: 20px;
        }
        .title {
        text-align: center;}
         </style>
        """, unsafe_allow_html=True)

    # Title Section
    st.markdown('<h1 class="title">❤️ Para mi Snoopy</h1>', unsafe_allow_html=True)
    st.divider()
    st.markdown('<div class="text">'
                '\n\nComo siempre hay que innovar, siempre me preguntas qué es lo que estoy haciendo, y me acuerdo de tu cara'
                'de pérdida cada vez que te intento explicar lo que estoy estudiando, asi que tu pollo se las ingenió para'
                'demostrarte cuanto te ama de la forma más pollesca 🐣 y pythonica 🐍 posible! '
                '\n Lista para la aventura? 🧐 Preparate mi peanut, esta aplicación es solo para ti\n\n</div>',
                unsafe_allow_html=True)
    st.divider()
    col1,col2,col3 = st.columns(3,gap='medium',border=True)

    with col1:
        st.markdown('<div class="custom_font"><h2>Música maestro</h2></div>', unsafe_allow_html=True)
        st.image("./images/music.jpg",use_container_width=True)
        if st.button(icon="🎤",use_container_width=True,label=''):
            st.switch_page('pages/1_🎤_music.py')

    with col2:
        st.markdown('<div class="custom_font"><h2>Por qué te amo?</h2></div>', unsafe_allow_html=True)
        st.image("./images/memories.jpg",use_container_width=True)
        if st.button(icon="❤️",use_container_width=True,label=''):
            st.switch_page('pages/2_❤️_love.py')

    with col3:
        st.markdown('<div class="custom_font"><h2>A pensar</h2></div>', unsafe_allow_html=True)
        st.image("./images/read.jpg",use_container_width=True)
        if st.button(icon="📖",use_container_width=True,label=''):
            st.switch_page('pages/3_📖_Read.py')


if __name__ == "__main__":
    main()


