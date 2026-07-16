# 🚗 Linear Regression Prediction with TensorFlow & Django

## 📖 Description

Ce projet est une application web développée avec **Django** et **TensorFlow** permettant de prédire la consommation de carburant (**MPG - Miles Per Gallon**) d'un véhicule à partir de ses caractéristiques techniques.

L'utilisateur saisit les informations d'une voiture dans un formulaire web. Ces informations sont ensuite transmises à un modèle de Machine Learning entraîné avec TensorFlow afin de produire une prédiction.

L'objectif principal de ce projet est de démontrer l'intégration d'un modèle de Machine Learning dans une application web Django tout en respectant une architecture logicielle propre.

---

# ✨ Fonctionnalités

- Interface web avec Django
- Formulaire de saisie des caractéristiques d'un véhicule
- Validation des données utilisateur
- Chargement automatique d'un modèle TensorFlow entraîné
- Prédiction en temps réel
- Affichage du résultat dans l'interface web
- Architecture modulaire
- Séparation entre la logique Django et la logique Machine Learning

---

# 🛠 Technologies utilisées

- Python 3.13
- Django 6
- TensorFlow / Keras
- Pandas
- NumPy
- Scikit-Learn
- Bootstrap 5
- uv (gestionnaire d'environnement Python)

---

# 📂 Structure du projet

```
linear-regression-tensorflow/
│
├── config/                 # Configuration Django
│
├── predictor/              # Application Django
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── ml/                     # Bibliothèque Machine Learning
│   ├── data/
│   │   └── auto-mpg.csv
│   │
│   ├── saved_models/
│   │   ├── model.keras
│   │   └── feature_columns.pkl
│   │
│   ├── preprocessing.py
│   ├── predictor.py
│   ├── schemas.py
│   ├── exceptions.py
│   └── train.py
│
├── static/
├── manage.py
├── pyproject.toml
└── README.md
```

---

# 🏗 Architecture générale

```
                 Utilisateur

                       │

                       ▼

               Formulaire Django

                       │

                       ▼

                Validation Django

                       │

                       ▼

                  CarFeatures

                       │

                       ▼

            RegressionPredictor

                       │

                       ▼

              TensorFlow (Keras)

                       │

                       ▼

                 Modèle entraîné

                       │

                       ▼

                 Valeur prédite

                       │

                       ▼

                 Interface HTML
```

---

# 📊 Dataset

Le projet utilise le célèbre dataset **Auto MPG**.

Variables utilisées :

| Variable | Description |
|----------|-------------|
| Cylinders | Nombre de cylindres |
| Displacement | Cylindrée |
| Horsepower | Puissance |
| Weight | Poids |
| Acceleration | Accélération |
| Model Year | Année du modèle |
| Origin | Pays d'origine |

Variable cible :

```
MPG (Miles Per Gallon)
```

---

# 🧹 Prétraitement des données

Le pipeline de préparation effectue :

- Chargement du dataset
- Suppression des valeurs manquantes
- Encodage One-Hot de l'origine
- Séparation Features / Labels
- Découpage Train/Test
- Création d'une couche de normalisation TensorFlow

Pipeline :

```
CSV

↓

Chargement

↓

Nettoyage

↓

One-Hot Encoding

↓

Train/Test Split

↓

Normalization

↓

TensorFlow
```

---

# 🧠 Modèle de Machine Learning

Le modèle est un réseau de neurones très simple composé de :

```
Normalization

↓

Dense(1)
```

Compilation :

- Optimizer : Adam
- Loss : Mean Squared Error (MSE)
- Metric : Mean Absolute Error (MAE)

---

# 🚀 Installation

## 1. Cloner le projet

```bash
git clone https://github.com/<username>/linear-regression-tensorflow.git

cd linear-regression-tensorflow
```

---

## 2. Installer les dépendances

```bash
uv sync
```

---

## 3. Entraîner le modèle

```bash
uv run python -m ml.train
```

Cette commande génère :

```
ml/saved_models/

model.keras

feature_columns.pkl
```

---

## 4. Lancer Django

```bash
uv run python manage.py runserver
```

Puis ouvrir :

```
http://127.0.0.1:8000
```

---

# 🖥 Déploiement

Le projet est conçu pour être déployé sur un serveur Linux.

Architecture cible :

```
Internet

↓

Nginx

↓

Gunicorn

↓

Django

↓

TensorFlow
```

---

# 📁 Description du dossier ml

## preprocessing.py

Préparation des données :

- Chargement
- Nettoyage
- Encodage
- Train/Test Split
- Normalisation

---

## train.py

Responsable de :

- Construire le modèle
- Compiler le modèle
- Entraîner
- Évaluer
- Sauvegarder

---

## predictor.py

Responsable de :

- Charger le modèle
- Préparer une observation
- Effectuer une prédiction

---

## schemas.py

Décrit les objets métier utilisés par le projet.

Exemple :

```python
CarFeatures
```

---

## exceptions.py

Contient les exceptions personnalisées.

Exemple :

```python
ModelNotLoadedError

InvalidOriginError
```

---

# 🔄 Cycle de vie complet

```
Dataset

↓

Prétraitement

↓

Entraînement

↓

Sauvegarde

↓

model.keras

↓

Application Django

↓

Chargement

↓

Prédiction

↓

Affichage
```

---

# 📚 Concepts Machine Learning abordés

- Régression linéaire
- TensorFlow
- Keras
- Normalisation
- One-Hot Encoding
- Train/Test Split
- Data Preprocessing
- Lazy Loading
- Data Validation

---

# 💡 Améliorations possibles

- API REST avec Django REST Framework
- Dockerisation
- Gunicorn + Nginx
- HTTPS avec Let's Encrypt
- Interface graphique améliorée
- Journalisation (Logging)
- Tests unitaires
- Pipeline CI/CD
- Support de plusieurs modèles

---

# 👨‍💻 Auteur

Projet réalisé dans le cadre de l'apprentissage de l'intégration du Machine Learning avec Django.

Technologies principales :

- Django
- TensorFlow
- Python
- Bootstrap
- Scikit-Learn

---

# 📄 Licence

Projet réalisé à des fins pédagogiques.
