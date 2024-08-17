import streamlit as st
import requests 

st.title("مصرف نکن")
r=requests.get("http://127.0.0.1:8000/Contents")
print(r.json())
for ad in r.json():
    for x,y in zip(ad.keys(),ad.values()) :
        st.html(f"<h1>{y}</h1>")