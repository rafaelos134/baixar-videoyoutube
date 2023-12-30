# from pytube import YouTube
# import streamlit as st
# from io import BytesIO
# import time

# title = st.text_input('coloque o link do youtube', '')

# def dowload_video(title):
#         yt = YouTube(title)
#         buffer = BytesIO()
#         video = yt.streams.get_by_itag(18)
#         video.stream_to_buffer(buffer)
#         buffer.seek(0)
#         return buffer

# def dowload_audio(title):
#     buffer = BytesIO()
#     youtube_video = YouTube(title)
#     audio = youtube_video.streams.get_audio_only()
#     audio.stream_to_buffer(buffer)
#     return buffer
     


# on = st.toggle('Somente audio')
# if title:
#     if on:
#         with st.spinner("Downloading Audio Stream from Youtube..."):
#             buffer = dowload_audio(title)
            
       

#     else:
#         with st.spinner("Downloading video Stream from Youtube..."):
#             buffer = dowload_video(title)
        
    
#     if on:
#         st.download_button(
#                             label="Download",
#                             data=buffer, 
#                             mime="audio/mpeg")
#         time.sleep(15) 
#     else:
#          st.download_button(
#                         label="Download",
#                         data=buffer, 
#                         mime="video/mp4") 
#          time.sleep(15) 






from pytube import YouTube
import streamlit as st
from io import BytesIO
import time

st.title('Baixar vídeos do _Youtube_')


title = st.text_input('coloque o link do youtube', '')

def dowload_video(title):
        yt = YouTube(title)
        buffer = BytesIO()
        video = yt.streams.get_highest_resolution()
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        return buffer,yt.title

def dowload_audio(title):
    buffer = BytesIO()
    youtube_video = YouTube(title)
    audio = youtube_video.streams.get_audio_only()
    audio.stream_to_buffer(buffer)
    return buffer,youtube_video.title
     


on = st.toggle('Somente audio')
if title:
    if on:
        with st.spinner("Carregando áudio..."):
            buffer,nome_video = dowload_audio(title)
        st.download_button(
                            label="Download",
                            data=buffer, 
                            mime="audio/mpeg",
                            file_name='{}.mp3'.format(nome_video))

            
       

    else:
        with st.spinner("Carregando vídeo..."):
            buffer,nome_video = dowload_video(title)
        st.download_button(
                        label="Download",
                        data=buffer, 
                        mime="video/mp4",
                        file_name='{}.mp4'.format(nome_video)) 
        