import streamlit as st
import requests
import json
import io

"""
# UberPred 🚕
"""

st.markdown(
    """
Envoie un fichier json avec 1000 trajets et je vais essayer de tout prédire 💸
"""
)

file = st.sidebar.file_uploader('Upload a JSON')

if st.sidebar.button('Prédis moi tout ça !'):

    url = "https://api.demo-marseille-lecture.com/pred1000/"

    bytes_data = file.getvalue()
    # st.write(bytes_data)

    stringio = io.StringIO(file.getvalue().decode("utf-8"))
    st.write(stringio)
    response = requests.post(url, files=file)
    print(response)
