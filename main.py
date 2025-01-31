import streamlit as st
pages = [
    st.Page("app_pages/home.py",title="home"),
    st.Page("app_pages/song.py",title="Song-downloader"),
    st.Page("app_pages/playlist.py",title="Playlist-downloader")]

pg = st.navigation(pages,position="hidden",expanded=True)


pg.run()







