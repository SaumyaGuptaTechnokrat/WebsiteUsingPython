import streamlit as st
import pandas as pd
import numpy as np
import requests
st.set_page_config(page_title="Cool Wesbite | Python",page_icon=":tada:",layout="wide")
# def load_lottieurl(url):
#fhfd
#     r=requests.get(url)
#     if r.status_code !=200:
#         return None
#     return r.json()

#---HEADER SECTION ----
#---To have content at center use layout="wide---

# lottie_coding=load_lottieurl("https://giphy.com/embed/2IudUHdI075HL02Pkk")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("Style/style.css")
with st.container():
    st.subheader("hi,I am Saumya Gupta:wave:")
    st.title("A Freelancer|Developer|Student From Lucknow")
    st.write("I am technokrat graduate enthusiast in Web Development")
    st.write("[Learn More >](https://linktr.ee/saumyatechnokrat)")
with st.container():
    st.write("---")
    left_colum,right_column = st.columns(2)
    
    with left_colum:
        st.header("What I do")
        st.write("#")
        st.write("""I am technokrat engineering graduate enthusiast in webdevelopment
                 one of my recent project is You_TubeCloneUsingReact
                 and another is SpeechToTextConverter
""")
        st.write("[YouTubeCloneUsingReact>](https://saumyaguptatechnokrat.github.io/YouTubeClone/)")
        st.write("[SpeechToTextConverterUsingReact>](https://saumyaguptatechnokrat.github.io/SpeechToTextConverter/)")
    with right_column:
        animation = """
    <img width="500vh" style="z-index:-1;border-radius:5px" alt="Coding_Animation" src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExb2h1aWRzMG44MHkxY3M5ZjF1bnh3aWljaml5OTV3dTBma2NqbDEzZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RbDKaczqWovIugyJmW/giphy.gif">
    """
        st.markdown(animation,unsafe_allow_html=True)
#---CONTACT---
with st.container():
    st.write("---")
    st.header("Get in touch With Me!!") 
    st.write("##")
    contact_form="""
    <form action="https://formsubmit.co/sgy4765@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" placeholder="Your Name" name="name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_colum,right_column=st.columns(2)
with left_colum:
    st.markdown(contact_form,unsafe_allow_html=True)
with right_column:
    st.empty()