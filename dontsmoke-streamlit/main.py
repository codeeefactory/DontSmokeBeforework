import streamlit as st
import requests 

st.title("مصرف نکن")
r=requests.get("http://127.0.0.1:8000/Contents")
for ad in r.json()[1]:
    st.write(ad)