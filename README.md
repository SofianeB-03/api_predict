# api_predict

https://github.com/SofianeB-03/api_predict


## Objectifs

- L'objectif de ce projet est de mettre en place un outil permettant de prédire la probabilité qu'un client remboursera son crédit
- Cet outil se base sur un modèle Machine Learning de classification supervisée
- Cet outil de prédiction sera mise en production à l’aide d’une API, et un dashboard interactif qui appelle cet API est mis en place afin de faciliter l'utilisation de cet outil via une interface graphique.


## Fonctionnalités

### API

A partir d'un identifiant client:
- on retourne la probabilité que ce client rembourse son crédit
- on retourne l'interprétabilité du modèle pour ce client i.e quelles variables ont le plus contribué à la prédicition


### Dashboard

- Selectionner l'ID d'un client depuis une liste déroulante
- Affichage des informations relatif au client séléctionné
- Comparaison du client avec l'ensemble des clients de la base
- Boutton "run prediction" qui appelle l'API pour calculer la probabilité que ce client rembourse son crédit


## Arborescence

./
└───api_predict
    │   basic_app.py
	│   clients_api.csv
	│   model.pkl
	│   README.md
	│   requirements.txt
	│   test_basic_app.py
	│   user_interface.py
	│   utils_ui.py
	│   X_train_DEBBUG.npz
	│   y_train_DEBBUG.npy
	│
	├───.github
	│   └───workflows
	│           ci.yml

C:.
├───.github
│   └───workflows
├───.pytest_cache
│   └───v
│       └───cache
└───__pycache__



- basic_app.py: le code de l'API
- test_basic_app.py: le code pour faire les tests unitaires de l'API
- user_interface.py: le code du dashboard
- utils_ui.py: des fonctions utiles pour le code du dashboard
- clients_api.csv: la base de clients
- ci.yml: le fichier de configuration pour automatiser dans un pipeline tout le processus de déploiement avec Github Action
- model.pkl: le modèle de scoring au format pickle
- X_train_DEBBUG.npz, y_train_DEBBUG.npy: des fichiers nécessaires pour l'interpretabilité du modèle