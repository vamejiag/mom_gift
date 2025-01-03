#imports
import streamlit as st
import random
from streamlit_player import st_player, _SUPPORTED_EVENTS
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import numpy as np
from googleapiclient.discovery import build
api_key = 'AIzaSyDKdfkX0A3dFIO4iUcZRPFXQSv7xyycpaE'
youtube = build("youtube", "v3", developerKey=api_key)


# Setup the authentication
client_id = '2e5e3dff9d86457b8ad2a0e26fea013b'
client_secret = '7d14a57deaa9495c9402504250bbbaef'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Define the playlists for each mood
playlists = {
    'happy': '2H1nfYzAsIVyDPmP7yqutd',
    'dance': '2H1nfYzAsIVyDPmP7yqutd',
    'energetic': '2H1nfYzAsIVyDPmP7yqutd',
    'english': '3J8htbKZUVpSfMISMGiff2',
    'instrumental': '1XUox3CNdUTQES399G7kze',
}

# List of possible artists for other moods
artists = [
    "morat",'luis miguel', "andres cepeda", "carlos vives", "abba", "queen", "disney songs",
    "fonseca", "shakira", "enrique iglesias", "juanes", "louane","morat",'juanes',
    "luis fonsi", "bacilos", "kany garcia", "chayanne", 'bruno mars', 'bachata', 'disney', 'tierra de osos'
]

moods = [
    "💪 Estoy Vive100",
    "😡 Me Enrabio",
    "🙏 Espíritu Santo Ilumíname",
    "😤 Dame Paciencia",
    "😊 Happy Happy",
    "😭 A Lagrima Tendida",
    "💖 Todo es Amor",
    "🌈 :rainbow[Rayo de Sol]",
    "🤷 No me aguanto ni yo",
    "🎲 Random"]

match_mood = ["energetic",
              "instrumental",
              "instrumental",
              "chill",
              "happy",
              "sad",
              'romantic',
              'dance',
              'chill',
              'english']

mood_map = dict(zip(moods, match_mood))

# Function to get songs from a playlist
def get_songs_from_playlist(playlist_id, limit=50):
    # Fetch the playlist's tracks using the Spotify API
    results = sp.playlist_items(playlist_id, limit=limit)

    # Get song details
    songs = []
    for track in results['items']:
        song_info = {
            'song': track['track']['name'],
            'artist': track['track']['artists'][0]['name'],
            'url': track['track']['external_urls']['spotify']
        }
        songs.append(song_info)

    return songs

# Function to search songs by artist if mood doesn't match a specific playlist
def search_songs_by_artist(mood_query,artist, limit=50):
    search_query = f"{mood_query} and {artist}"
    # Use the YouTube API to search for videos
    request = youtube.search().list(
        part="snippet",
        q=search_query,
        type="video",
        videoCategoryId="10",  # Music category
        maxResults=30  # Limit to top 30 results
    )
    response = request.execute()
    # Process the response and extract video URLs
    songs = []
    for item in response['items']:
        video_info = {
            'song': item['snippet']['title'],
            'artist': item['snippet']['channelTitle'],
            'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        }
        songs.append(video_info)
    return songs


# Function to search for YouTube videos by mood
def search_youtube_url(songs):
    search_query = f"{songs['song']} and {songs['artist']}"
    # Use the YouTube API to search for videos
    request = youtube.search().list(
        part="snippet",
        q=search_query,
        type="video",
        videoCategoryId="10",  # Music category
        maxResults=5  # Limit to top 5 results
    )

    response = request.execute()

    # Process the response and extract video URLs
    videos = []
    for item in response['items']:
        video_info = {
            'title': item['snippet']['title'],
            'channel': item['snippet']['channelTitle'],
            'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        }
        videos.append(video_info)
    return videos[0]['url']

# Function to get songs based on the selected mood
def get_song_recommendations(mood):
    # Check if the mood matches a predefined playlist
    if mood in playlists:
        playlist_id = playlists[mood]
        songs = get_songs_from_playlist(playlist_id, limit=30)
    else:
        # If mood does not match a predefined playlist, choose a random artist from the list
        random_artist = random.choice(artists)
        songs = search_songs_by_artist(mood,random_artist, limit=30)
    #print(len(songs))
    id = np.random.randint(1, 29)

    spotify_song = songs[id]
    print(spotify_song)
    url = search_youtube_url(spotify_song)
    return url

######################################################################

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
    selected_mood = st.radio("Selecciona tu estado de ánimo", moods, key="mood_selectbox",
                                 label_visibility="collapsed")
    selected_mood = mood_map[selected_mood]
    print(selected_mood)
    st.markdown("</div>", unsafe_allow_html=True)


with col3:
    if selected_mood:
        st.markdown(
            f"<div class='pink-style'>{selected_mood}</div>",
            unsafe_allow_html=True
        )
        song_url = get_song_recommendations(selected_mood)
    st.markdown("</div>", unsafe_allow_html=True)

    options = {
        "progress_interval": 1000,
        "volume": st.slider("Volume", 0.0, 1.0, 1.0, .01),
        "playing": st.checkbox("Playing", False),
        "muted": st.checkbox("Muted", False),
    }

    url = st.text_input("URL", song_url)
    event = st_player(url, **options, key="youtube_player")
