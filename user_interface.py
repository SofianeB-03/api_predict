# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 17:06:25 2023

@author: sofia
"""

import streamlit as st
#import json
#import requests
from fastapi.testclient import TestClient
from basic_app import app

# on va créer une interface graphique pour l'utilisateur (UI) permettant 
# de simplifier l'utilisation de notre API servant les services de prédiction
# de la classe d'un client et de l'interprétabilité


# Make page
st.set_page_config(page_title="WELCOME TO MY API")
st.header("Credit Customer Prediction Project")


idx_client = st.sidebar.text_input("Enter the ID of the client : ")

if st.sidebar.button('Run'):
    
    # url où se trouve l'endpoint à tester
    url_endpoint_predict = '/predict'
    url_endpoint_interpret = '/interpretability'
    

    client = TestClient(app)
    # idx_client = 280777
    
    response_predict = client.post(url_endpoint_predict, json={'idx_client': idx_client})
    response_interpret = client.post(url_endpoint_interpret, json={'idx_client': idx_client})
    
    st.write("Prediction : ",response_predict.text)
    st.write("Interpretability : ",response_interpret.text)