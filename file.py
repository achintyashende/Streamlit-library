import streamlit as st
import pandas as pd

st.subheader("Uploading the CSV file")
df = st.file_uploader("Upload .csv file : ", type=['csv', 'xlsx'])

st.subheader("Loading the CSV file")

df = pd.read_csv('C:/Users/achin/.streamlit/Products.csv')
if df is not None:
    st.table(df.head())

st.subheader("Dealing with image file")
img = st.file_uploader("Upload an image : ", type=['jpg', 'png'])
if img is not None:
    st.image(img)

st.subheader("Working with video file")
vid = st.file_uploader("Upload an video : ", type=['mkv', 'mp4'])
if vid is not None:
    st.video(vid, start_time=0)

st.subheader("Working with audio file")
aud = st.file_uploader("Upload an Audio : ", type=['wav', 'mp3'])
if aud is not None:
    st.audio(aud.read())

st.subheader("Working with CSV file")
fil = st.file_uploader("Upload an CSV : ", type=['csv'])
if fil is not None:
    new = pd.read_csv(fil)
    st.table(new.head())
    