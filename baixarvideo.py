from pytube import YouTube
import streamlit as st

title = st.text_input('coloque o link do youtube', '')
on = st.toggle('Somente audio')


if on:
    try:
        yt = YouTube("{}".format(title))
        video = yt.streams.filter(only_audio=True)[0]
    except:
        st.write("Insira o link do youtube")

else:
    try:
        yt = YouTube("{}".format(title))
        video = yt.streams.get_highest_resolution()
    except:
        st.write("Insira o link do youtube")


if st.button('baixar'):
    try:
        video.download()
    except:
        st.write("Insira o link do youtube")

