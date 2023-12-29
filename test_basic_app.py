# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 18:53:00 2023

@author: sofia
"""


import pytest
from basic_app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_main():
    
    url_endpoint = '/'
    response = client.get(url_endpoint)
    
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to my API'}
    

# test de l'endpoint /predict dans l'API qui permet de faire la prédiction
def test_prediction():
        
    # url où se trouve l'endpoint à tester
    url_endpoint = '/predict'
    
    # envoie une requete avec la valeur idx_client au serveur où se trouve l'endpoint
    # et stocke la reponse du serveur dans la variable response (dict json)
    idx_client = 280777
    response = client.post(url_endpoint, json={'idx_client': idx_client})
    
    # vérifier que la requete a marché
    assert response.status_code == 200
    
    data_response = response.json()
    
    # vérifier qu'on a bien les champs class et proba dans la réponse
    assert 'class' in data_response
    assert 'proba' in data_response
    
    # vérifier qu'on a en retour les valeurs attendues
    # assert data_response['class'] == 0
    # assert data_response['proba'] == 0.73
    

# test de l'endpoint /interpretability dans l'API qui permet de faire l'interpretabilité
def test_interpretability():
        
    # url où se trouve l'endpoint à tester
    url_endpoint = '/interpretability'
    
    # envoie une requete avec la valeur idx_client au serveur où se trouve l'endpoint
    # et stocke la reponse du serveur dans la variable response (dict json)
    idx_client = 280777
    response = client.post(url_endpoint, json={'idx_client': idx_client})
    
    # vérifier que la requete a marché
    assert response.status_code == 200
    
    data_response = response.json()
    
    # vérifier qu'on a bien les champs class et proba dans la réponse
    assert 'interpretation' in data_response
    
    
    
"""
def print_response():
    from fastapi.testclient import TestClient
    client = TestClient(app)
    response = client.get('/')
                        
    # url où se trouve l'endpoint de l'api 
    #url_endpoint = 'http://127.0.0.1:8000/predict'
    
    # envoie une requete avec la valeur idx_client au serveur où se trouve l'endpoint
    # et stocke la reponse du serveur dans la variable response (dict json)
    #idx_client = 280777s
    #response = requests.post(url_endpoint, params={'idx_client': idxz_client})
    
    print(response.json())
    


if __name__ == '__main__':
    #pytest.main()
    #print_response()
    #test_prediction()
"""