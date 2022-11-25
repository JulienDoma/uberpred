import streamlit as st
import requests
import pandas as pd


"""
# UberPred - Predicition de masse 🚕
"""

st.markdown(
    """
Bienvenue, entre ton fichier à gauche et tu verras combien ça te coûte 💸
"""
)

file = st.sidebar.file_uploader('Choisir mon fichier (json expected)')

if st.sidebar.button('Combien ça me coûte ?'):

    url = "https://api.demo-marseille-lecture.com/pred1000/"
    response = requests.post(url, files={"file": file.getvalue()}).json()

    df = pd.DataFrame({k:pd.Series(v) for k, v in response.items()})

    st.table(df)

    somme = round(df['fare'].sum(),2)

    st.text(f'Le total de vos courses va coûter {somme} $')
