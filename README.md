# Plateforme-de-Traduction-Securisee-Fullstack-Backend






## Objectif du projet

Le backend a pour rôle central de fournir une API sécurisée et fiable pour la traduction de textes entre le français et l’anglais, tout en garantissant que seules les personnes authentifiées peuvent y accéder


## Structure du projet
```
backend/
│
├── models/
│   └── model.py      
│
├── tests/
│   └── test_endpoint.py   
│
├── .env             
├── .gitignore       
├── auth.py         
├── translate.py       
├── config.py        
├── database.py      
├── main.py         
│
├── Dockerfile             
├── docker-compose.yml     
│
├── requirements.txt      
└── README.md             

```


---

## Installation

1. Cloner le dépôt GitHub :  

```shell
    git clone https://github.com/elhidarinouhayla/Plateforme-de-Traduction-S-curis-e-Fullstack-Backend.git
    cd project
```

2. Créer un environnement virtuel :

 - Linux / Mac :
```shell
    python -m venv venv
    source venv/bin/activate
```
 - Windows :
```shell
    python -m venv venv
    venv\Scripts\activate
```

3. Installer les dépendances :

```shell
    pip install -r requirements.txt
```

4. Lancer l’API en mode développement :

```shell
    uvicorn main:app --reload
```

 - L’API sera accessible à l’adresse : http://127.0.0.1:8000

 - Documentation interactive Swagger : http://127.0.0.1:8000/docs

Astuce : Le paramètre --reload permet à l’API de se mettre à jour automatiquement à chaque modification du code, très pratique pour le développement.


## Configuration

```shell
HF_TOKEN=ton_token_huggingface
SECRET_KEY=une_clef_secrete
ALGORITHM=HS256
```
## Endpoint:/register

POST /register
Body JSON:
 
```shell
{
  "username": "admin",
  "password": "abcd"
}
```


## Endpoint:/login

POST /login

Authentification
Body JSON:

```shell
{
  "username": "admin",
  "password": "abcd"
}
```

Reponse:

```shell
{
  "token": "xxxxx.yyyyy.zzzzz"
}
```

## Endpoit:/translate

POST/translate
Protégé : nécessite JWT dans le header Authorization: Bearer <JWT>

Body JSON :

```shell
{
  "text": "Bonjour",
  "direction": "fr-en"
}
```
Response JSON:

```shell
{
  "translation": "Hello"
}
```




## Tests Unitaires

Les tests vérifient :

 - endpoint register
 - endpoint login
 - endpoint translate



### Commande pour lancer les tests :

```shell
pytest
```

## Dockerfile

Le Dockerfile permet de construire une image Docker pour le backend FastAPI.


Il fait les étapes suivantes :

  1. Utilise Python 3.11 slim comme base

  2. Définit le dossier de travail /app

  3. Copie le fichier requirements.txt et installe les dépendances Python

  4. Copie tout le code du backend dans l’image

  5. Expose le port 8000 pour l’API

  6. Lance le serveur Uvicorn à l’intérieur du conteneur

=> Cela permet de déployer facilement l’API sur n’importe quelle machine sans config supplémentaire

