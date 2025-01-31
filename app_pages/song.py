import streamlit as st
from yt_dlp import YoutubeDL
import os

st.markdown("""<style>
            [data-testid="stAppViewContainer"]{
            background-image: radial-gradient(circle, #6be81f, #00ea7e, #00e6bb, #00dee4, #00d3f3, #00d4f0, #00d6ee, #00d7eb, #00e5d3, #5beead, #a1f280, #e6f058);
            }
            </style>""",unsafe_allow_html=True)

header = "🎶SONG-DOWNLOADER"
span_element = ""
animation_styles = ""
for i,letter in enumerate(header):
    delay = i * 0.05
    span_element += f"<span class='letter{i}'>{letter}</span>"
    animation_styles += f"""
                        .letter{i}{{
                        animation : appear 1s {delay}s forwards;
                        }}  
                        """

#CSS STYLER
st.markdown(f"""
    <style>
        @keyframes appear {{
            0% {{
                opacity: 0;
            }}
            100% {{
                opacity: 1;
            }}
        }}
     .title {{
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            color : white !important;
            text-shadow: 2px 2px 0px black;
            text-shadow: 3px 3px 1px red;
        }}

        .title span {{
            display: inline-block;
            opacity: 0;
        }}

        .stButton>button,.fadein,.stTextInput ,.l1{{
            opacity: 0;
            animation: fadeInContent 2s 2s forwards;
        }}

        @keyframes fadeInContent {{
            0% {{
                opacity: 0;
            }}
            100% {{
                opacity: 1;
            }}
        }}

        {animation_styles}

        .stButton>button{{
            display: block;
            background-color: white !important;
            margin-top: 10px;
            margin-left: auto;
            margin-right: auto;
            color: red;
            font-weight: bold !important;
            font-size: 40px !important;
            border: 4px solid red;
            width: 300px;
            padding: 20px;
            transition: 0.3s,transform 0.2s;
        }}
        .stButton>button:hover{{
            
            background-color : #1FF307  !important;
            width: 350px;
            padding: 30px;
            color: white !important;
            border: 4px solid white !important;
            transform: scale(0.2s);
            

        }}
    </style>
""", unsafe_allow_html=True)

# Title with letter-by-letter animation
st.markdown(f"<h1 class='title'>{span_element}</h1>", unsafe_allow_html=True)



st.markdown("""
            <style>
                .l1{
                    font-size:25px!important;
                    margin-bottom:-60px;
                    font-weight:bold;
                }
            </style>
            """,unsafe_allow_html=True)
st.markdown("<p class='l1'>Enter Song Name : </p>",unsafe_allow_html=True)
name = st.text_input("Enter Song",key="name",label_visibility="hidden")



def song_downloader():
    if name:
        search_query = f"ytsearch:{name}"
        audiodownloader = {
            'format': 'bestaudio/best',
            'quiet': True,
            'audio-format': 'mp3',
            'outtmpl': f'{name}.mp3',  # Use title and extension dynamically
        }
        with YoutubeDL(audiodownloader) as downloader:
            info = downloader.extract_info(search_query,download=True)
            if info:
                song_name = info.get('title')
                artist = info.get('uploader')
        
        # Find the file that yt-dlp downloaded
        file_name = f"{name}.mp3"
        if os.path.exists(file_name):
            st.markdown(f"<p style='text-align: center;'>{song_name} Song Found .Press the button below to Download👇.</p>",unsafe_allow_html=True)
            with open(file_name, "rb") as file:
                st.markdown("""
                            <style>
                            .stDownloadButton { 
                                display: flex; 
                                justify-content: center; 
                            }
                            </style>
                            """, unsafe_allow_html=True)
                if st.download_button(label=f"⬇️Download {song_name}",
                                data=file,
                                file_name=file_name,
                                mime="audio/mp3"):
                    return 1
                
                
        else:
            st.warning("Download failed!")

    else:
        st.warning("Invalid Name!!")

# Button to start downloading
if st.button("Search"):
    if name:
        with st.spinner('Searching the song...'):
            a = song_downloader()
        if a == 1:
            st.success("Download Successful!")
    else:
        st.error("🚨Please enter a song name.")


if st.button("Home"):
    st.switch_page("app_pages/home.py")
