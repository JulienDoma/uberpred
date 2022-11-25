import streamlit as st
import requests
import pandas as pd


"""
# UberPred - Predicition de masse 🚕
"""

st.markdown(
"""
Entre ton fichier à gauche et tu verras combien ça te coûte 💸
"""
)
st.sidebar.write("Fichiers d'exemple à télécharger pour utiliser l'application")
with open("raw_data/pred10.json", "rb") as dl_file1:
    btn = st.sidebar.download_button(
            label="Fichier de 10 courses",
            data=dl_file1,
            file_name="pred10.json",
            mime="application/json"
          )

with open("raw_data/pred1000.json", "rb") as dl_file1:
    btn2 = st.sidebar.download_button(
            label="Fichier de 1000 courses",
            data=dl_file1,
            file_name="pred1000.json",
            mime="application/json"
            )

file = st.sidebar.file_uploader('Choisir mon fichier (json expected)')

if st.sidebar.button('Combien ça me coûte ?'):

    url = "https://api.demo-marseille-lecture.com/pred1000/"
    response = requests.post(url, files={"file": file.getvalue()}).json()

    df = pd.DataFrame({k:pd.Series(v) for k, v in response.items()})
    df.columns = ["Prix"]

    st.table(df)

    somme = round(df['Prix'].sum(),2)

    st.text(f'Le total de vos courses va coûter {somme} $')
