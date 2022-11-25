import streamlit as st
from datetime import datetime
import requests
import pandas as pd

"""
# UberPred 🚕
"""

st.markdown(
    """
Bienvenue, entre ton adresse de départ et ton adresse d'arrivée, tu verras combien ça te coûte 💸
"""
)

date = st.sidebar.date_input("Date du voyage")
time = st.sidebar.time_input("Heure du voyage")

geo_url = "https://maps.googleapis.com/maps/api/geocode/json"
pickup = st.sidebar.text_input("Adresse de départ : ")
dropoff = st.sidebar.text_input("Adresse d'arrivée : ")

passenger_count = int(
    st.sidebar.slider("Nombre de passagers", min_value=1, max_value=8, step=1, value=1)
)

if st.sidebar.button('Combien ça me coûte ?'):

    apikey = st.secrets['api_key']
    def get_pickup():
        # Récupérer les points cardinaux de l'adresse de départ
        params = {'key': apikey, 'address': pickup}

        response = requests.get(geo_url, params=params).json()

        pickup_longitude = response['results'][0]['geometry']['location']['lng']
        pickup_latitude = response['results'][0]['geometry']['location']['lat']

        return pickup_longitude, pickup_latitude

    def get_dropoff():
        # Récupérer les points cardinaux de l'adresse d'arrivée
        params = {'key': apikey, 'address': dropoff}

        response = requests.get(geo_url, params=params).json()

        dropoff_longitude = response['results'][0]['geometry']['location']['lng']
        dropoff_latitude = response['results'][0]['geometry']['location']['lat']

        return dropoff_longitude, dropoff_latitude

    pickup_longitude, pickup_latitude = get_pickup()
    dropoff_longitude, dropoff_latitude = get_dropoff()

    pickup_datetime = str(datetime.combine(date, time).strftime("%Y-%m-%d %H:%M:%S"))

    url = "https://api.demo-marseille-lecture.com/predict"

    parameters = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count,
    }

    response = requests.get(url, params=parameters).json()
    st.write("Prix : " + str(round(response["fare"], 0)) + " $")

    df = pd.DataFrame(
        {
            'lat':[float(pickup_latitude), float(dropoff_latitude)],
            'lon' :[float(pickup_longitude), float(dropoff_longitude)]
        }
    )

    st.map(df)
