#imports
import streamlit as st
import random
from streamlit_player import st_player, _SUPPORTED_EVENTS

# intro
st.set_page_config(page_title="Música maestro",
                   page_icon="🎤",layout='wide',
                   )

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
    .centered-text {
        text-align: center;
    }
    .pink-style {
        background-color: #ffd6e5;
        border-radius: 10px;
        padding: 15px;
    }
    .light-blue-style {
        background-color: #d6ecff;
        border-radius: 10px;
        padding: 15px;
    }
    // this is for all img elements in the Streamlit div class nesting a img
    .css-1v0mbdj > img{
      border-radius: 50%;
    }
  </style>
  
    </style>
""", unsafe_allow_html=True)



st.markdown("# 🎤 Música maestro")
st.divider()

text = """...\n\nDepresiva? Animada? ¿Ganas de meternos en el carro sin rumbo y cantar a todo pulmón? 
    Elige tu mood y deja que telepáticamente elija la canción que cantaremos juntas.
    """
st.markdown(f"<div class='box-style'> <br>¿Depresiva?<br> Animada? <br>¿Ganas de meternos en el carro sin rumbo y "
            f"cantar a todo pulmón?<br> Elige tu mood y deja que telepáticamente elija la canción que cantaremos "
            f"juntas<br>...</div>", unsafe_allow_html=True)

st.divider()
# Create two columns: one for the image and dropdown, and the other for the mood text
col1, col2,col3 = st.columns([0.3, 0.25, 0.25],gap='medium',border=True)

# Left column (image and dropdown centered)
with col1:
    # Display the image
    st.image("./images/music.jpg", use_container_width=True)  # Update with your image path

with col2:
    st.markdown("<div class='pink-style'> Selecciona tu mood del día :", unsafe_allow_html=True)
    st.markdown('\n\n')
    # Mood options in the dropdown
    moods = [
        "💪 Estoy Vive100", "😡 Me Enrabio", "🙏 Espíritu Santo Ilumíname",
        "😤 Dame Paciencia", "😊 Happy Happy", "😭 A Lagrima Tendida",
        "💖 Todo es Amor", "🌈 :rainbow[Rayo de Sol]", "🤷 No me aguanto ni yo",
        "🎲 Random"
    ]
    selected_mood = st.radio("Selecciona tu estado de ánimo", moods, key="mood_selectbox",
                                 label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)


with col3:
    if selected_mood:
        st.markdown(
            f"<div class='pink-style'>{selected_mood}</div>",
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

    options = {
        "progress_interval": 1000,
        "volume": st.slider("Volume", 0.0, 1.0, 1.0, .01),
        "playing": st.checkbox("Playing", False),
        "muted": st.checkbox("Muted", False),
    }

    url = st.text_input("URL", "https://soundcloud.com/imaginedragons/demons")
    event = st_player(url, **options, key="soundcloud_player")
