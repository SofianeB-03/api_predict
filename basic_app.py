# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:42:47 2023

@author: sofia
"""

from fastapi import FastAPI
import uvicorn
import pandas as pd
import pickle
import lime.lime_tabular  
import numpy as np    

from pydantic import BaseModel

# Declaring our FastAPI instance
app = FastAPI()
 
# Defining path operation for root endpoint
@app.get('/')
def main():
    return {'message': 'Welcome to my API'}
 
# Defining path operation for /name endpoint
#@app.get('/{name}')
#def hello_name(name : str): 
    # Defining a function that takes only string as input and output the
    # following message. 
    #return {'message': f'Welcome to GeeksforGeeks!, {name}'}



class request_body(BaseModel):
    idx_client : int
    

clients = pd.read_csv("clients_api.csv")
name_features = clients.drop(columns="SK_ID_CURR").columns

X_train_DEBBUG = np.load("X_train_DEBBUG.npz")
X_train_DEBBUG = X_train_DEBBUG['arr_0']

y_train_DEBBUG = np.load("y_train_DEBBUG.npy")

# path_model = r"C:\Users\sofia\mlartifacts\468947715740038560\3566fd9bc64047adbefb403f3f357e13\artifacts\model\model.pkl"
path_model = "model.pkl"

best_model = pickle.load(open(path_model, 'rb'))

best_seuil = 0.4
    

@app.post('/predict')
def predict(data : request_body):
    
    test_data = clients[clients["SK_ID_CURR"]==data.idx_client].drop(columns="SK_ID_CURR")
    test_data = test_data.to_numpy()
        
    # probabilité des classes 0 et 1
    #y_pred_proba = best_model.predict_proba(test_data)
    
    proba_class_0 = best_model.predict_proba(test_data)[0][0]   
    proba_class_1 = best_model.predict_proba(test_data)[0][1]
    
    if proba_class_1 >= best_seuil:
        class_idx = 1
        class_proba = proba_class_1
    else:
        class_idx = 0
        class_proba = proba_class_0
    
    class_proba = round(class_proba,2)
    
    # prédiction de la classe selon le seuil
    # class_idx = proba_to_class(y_pred_proba, best_seuil)
    #class_idx =  class_idx[0]
    
    # probabilité de la classe prédite
    #proba_class = y_pred_proba[class_idx]
    
    return { 'class' : class_idx, 'proba': class_proba}
    


@app.post('/interpretability')
def interpretability(data : request_body):
    
    test_data = clients[clients["SK_ID_CURR"]==data.idx_client].drop(columns="SK_ID_CURR")
    test_data = test_data.to_numpy()

    explainer = lime.lime_tabular.LimeTabularExplainer(X_train_DEBBUG, mode='classification',
                                                       training_labels=y_train_DEBBUG, 
                                                       feature_names=name_features)
    explanation = explainer.explain_instance(test_data[0], best_model.predict_proba)
    
    
    return { 'interpretation' : explanation.as_list()}
