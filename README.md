# 🚗 Linear Regression Prediction with TensorFlow & Django

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![uv](https://img.shields.io/badge/Package_Manager-uv-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

# 📖 Description

**Linear Regression Prediction with TensorFlow & Django** est une application Web développée en Python qui démontre l'intégration d'un modèle de Machine Learning dans une application Django.

Le projet permet à un utilisateur de saisir les caractéristiques d'un véhicule via une interface Web.

Les données sont ensuite transmises à un modèle de régression linéaire développé avec **TensorFlow/Keras**, qui estime la consommation de carburant (**MPG - Miles Per Gallon**).

L'objectif principal du projet est de montrer comment intégrer proprement un modèle de Machine Learning dans une application Web moderne tout en respectant une architecture logicielle claire et maintenable.

---

# ✨ Fonctionnalités

- Interface Web développée avec Django
- Formulaire de saisie ergonomique
- Validation des données utilisateur
- Chargement paresseux (Lazy Loading) du modèle TensorFlow
- Prédiction en temps réel
- Affichage du résultat dans l'interface
- Architecture modulaire
- Séparation entre la logique métier et la logique Machine Learning
- Déploiement sur AWS EC2
- Utilisation de Gunicorn et Nginx

---

# 🎯 Objectifs pédagogiques

Ce projet couvre plusieurs domaines :

- Développement Web avec Django
- Machine Learning avec TensorFlow
- Prétraitement des données
- Régression Linéaire
- Déploiement Linux
- Administration système
- Architecture logicielle
- DevOps

---

# 🛠 Technologies utilisées

| Technologie | Utilisation |
|-------------|------------|
| Python 3.13 | Langage principal |
| Django 6 | Framework Web |
| TensorFlow | Machine Learning |
| Keras | Construction du modèle |
| Pandas | Manipulation des données |
| NumPy | Calcul scientifique |
| Scikit-Learn | Découpage Train/Test |
| Gunicorn | Serveur WSGI |
| Nginx | Reverse Proxy |
| uv | Gestionnaire d'environnement Python |
| AWS EC2 | Déploiement |

---

# 🏗 Architecture générale

```
                       Utilisateur

                            │

                            ▼

                  Navigateur Web

                            │

                            ▼

                         Nginx

                            │

                            ▼

                     Gunicorn WSGI

                            │

                            ▼

                         Django

                            │

                            ▼

                  RegressionPredictor

                            │

                            ▼

                   TensorFlow / Keras

                            │

                            ▼

                     model.keras

                            │

                            ▼

                   Valeur prédite (MPG)
```

---

# 📂 Structure du projet

```
linear-regression-tensorflow/

│

├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── predictor/
│   ├── templates/
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── ml/
│   ├── data/
│   │
│   ├── saved_models/
│   │   ├── model.keras
│   │   └── feature_columns.pkl
│   │
│   ├── preprocessing.py
│   ├── predictor.py
│   ├── train.py
│   ├── schemas.py
│   └── exceptions.py
│
├── static/
│
├── manage.py
│
├── pyproject.toml
│
└── README.md
```

---

# 🚀 Fonctionnement global

Le cycle complet est le suivant :

```
Utilisateur

↓

Formulaire Django

↓

Validation

↓

Création de CarFeatures

↓

RegressionPredictor

↓

Préparation des données

↓

TensorFlow

↓

Prédiction

↓

Retour vers Django

↓

Affichage du résultat
```

---

# 📊 Dataset

Le projet utilise le célèbre dataset :

**Auto MPG Dataset**

Variables utilisées :

| Variable | Description |
|-----------|------------|
| Cylinders | Nombre de cylindres |
| Displacement | Cylindrée |
| Horsepower | Puissance |
| Weight | Poids |
| Acceleration | Accélération |
| Model Year | Année |
| Origin | Pays d'origine |

Variable cible :

```
MPG
```

---

# 🧠 Modèle de Machine Learning

Le modèle est constitué de seulement deux couches :

```
Normalization

↓

Dense(1)
```

Optimizer :

```
Adam
```

Loss :

```
Mean Absolute Error
```

---

# 🧹 Prétraitement

Le pipeline réalise automatiquement :

- Chargement du CSV
- Nettoyage des données
- Suppression des valeurs manquantes
- Encodage One-Hot de l'origine
- Train/Test Split
- Création du Normalizer TensorFlow

Pipeline :

```
CSV

↓

Pandas

↓

Cleaning

↓

Encoding

↓

Train/Test Split

↓

Normalization

↓

TensorFlow
```

---

# ⚙ Installation locale

## Cloner

```bash
git clone https://github.com/<username>/linear-regression-tensorflow.git

cd linear-regression-tensorflow
```

---

## Installer uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## Installer les dépendances

```bash
uv sync
```

---

## Entraîner le modèle

```bash
uv run python -m ml.train
```

---

## Lancer Django

```bash
uv run python manage.py migrate

uv run python manage.py runserver
```

---

# ☁ Déploiement

Le projet est prévu pour fonctionner sur une instance Linux sans interface graphique.

Architecture de production :

```
Internet

↓

Port 80

↓

Nginx

↓

Gunicorn

↓

Socket Unix

↓

Django

↓

TensorFlow
```

Le socket Unix est créé dans :

```
/run/gunicorn/
```

---

# 🔒 Sécurité

- Reverse Proxy Nginx
- Gunicorn isolé
- Validation Django Forms
- Validation métier via `CarFeatures`
- Exceptions personnalisées
- Socket Unix au lieu d'un port TCP interne

---

# 📚 Documentation

Une documentation détaillée est disponible :

- ARCHITECTURE.md
- ML.md
- DJANGO.md
- DEPLOYMENT.md
- API.md
- CONTRIBUTING.md
- FAQ.md

---

# 📈 Améliorations futures

- API REST (Django REST Framework)
- Docker
- Docker Compose
- Kubernetes
- CI/CD GitHub Actions
- Tests unitaires
- Tests d'intégration
- HTTPS avec Let's Encrypt
- Authentification utilisateur
- Historique des prédictions
- Plusieurs modèles TensorFlow

---

# 👨‍💻 Auteur
- Mamadou Yassarou Diallo

Projet réalisé dans le cadre de l'apprentissage de l'intégration du Machine Learning avec Django.

---

# 📄 Licence

Ce projet est distribué sous licence MIT.

Voir le fichier LICENSE.
