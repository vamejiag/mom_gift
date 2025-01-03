#imports
import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
import requests


#Intro
st.set_page_config(page_title="The petite section",
                   page_icon="🐣👩‍💻",
                   layout="centered")

# App title
st.title("Streamlit App: Future Ideas and Updates")

# Divider
st.markdown("---")

# Section: Future Ideas
st.header("🌟 Future Ideas for the App")

# Subsection: Recommendations Based on AI
st.subheader("🎵 Recommendations Based on AI")
st.markdown("""
Inspired by [Building a Content-Based Song Recommendation Website](https://meysamraz.medium.com/building-a-content-based-song-recommendation-website-in-python-from-spotifys-songs-data-fc36b6204a37), we aim to:

- Leverage advanced AI techniques to offer personalized song recommendations.
- Continuously update the recommendation engine to adapt to user preferences.
- [Example](https://mood-music.streamlit.app/)
""")

# Subsection: Turn Messages Into Voice Messages
st.subheader("🔊 Turn Messages Into Voice Messages")
st.markdown("""
- Add a feature to convert text messages into voice messages.
  - **Risks**: Potential misuse for creating deep fakes.
""")

# Subsection: Storytelling From Images
st.subheader("🖼️ Storytelling From Images")
st.markdown("""
- Develop an option to create engaging stories from user-provided images.
- Use natural language generation to tell personalized tales.
""")

# Subsection: Training AI on Personal Data
st.subheader("🤖 Training AI on Personal Data")
st.markdown("""
For a more tailored experience:
- Train an AI to learn from user-specific data.
- Generate reasons "Why I Love Her," capturing unique user traits.
- Use techniques like:
  - **Prompt Tuning**
  - **Fine-Tuning**
""")

# Divider
st.markdown("---")

# Section: How to Train AI for Fine-Tuning
st.header("🛠️ How to Train AI for Fine-Tuning")

st.markdown("""
### Resources to Explore:

1. [Fine-Tuning Tutorial in Google Colab](https://colab.research.google.com/drive/14xo6sj4dARk8lXZbOifHEn1f_70qNAwy?usp=sharing#scrollTo=cg3fiQOvmI3Q)
   - Step-by-step guidance on setting up fine-tuning workflows.

2. [Hugging Face Fine-Tuning](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407)
   - Models and tools for fine-tuning powerful AI frameworks.
""")

# Divider
st.markdown("---")

# Section: Overcoming Challenges
st.header("💡 Overcoming Challenges")

st.subheader("🔧 Google Colab Fails")
st.markdown("""
Referencing my troubleshooting experience:

- [All My Google Colab Fails](https://colab.research.google.com/drive/1MrESk3Y-AtFef1B_5hYbbAvi5LQzp2IA?authuser=1#scrollTo=wltw35lK8CCU)
  - Insights from my failed attempts.
  - Lessons learned? and adjustments for future success.
""")

# Divider
st.markdown("---")

# Section: Vision for the Future
st.header("🌈 Vision for the Future")
st.markdown("""
none""")

# Divider
st.markdown("---")