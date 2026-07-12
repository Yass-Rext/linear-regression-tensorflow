"""
Prétraitement des données Auto MPG.

Ce module est responsable de :

- Charger le dataset
- Nettoyer les données
- Encoder les variables catégorielles
- Séparer Features / Labels
- Construire le Normalizer TensorFlow
"""

from pathlib import Path

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split


# ------------------------------------------------------------------
# Constantes
# ------------------------------------------------------------------

BASE_DIR = Path(__file__).parent

DATASET_PATH = BASE_DIR / "data" / "auto-mpg.csv"

COLUMN_NAMES = [
    "MPG",
    "Cylinders",
    "Displacement",
    "Horsepower",
    "Weight",
    "Acceleration",
    "Model Year",
    "Origin",
]

ORIGIN_MAPPING = {
    1: "USA",
    2: "Europe",
    3: "Japan",
}


# ------------------------------------------------------------------
# Chargement
# ------------------------------------------------------------------

def load_dataset() -> pd.DataFrame:
    """
    Charge le dataset Auto MPG.
    """

    dataset = pd.read_csv(
        DATASET_PATH,
        names=COLUMN_NAMES,
        na_values="?",
        comment="\t",
        sep=r"\s+",
        skipinitialspace=True,
    )

    return dataset


# ------------------------------------------------------------------
# Nettoyage
# ------------------------------------------------------------------

def clean_dataset(dataset: pd.DataFrame) -> pd.DataFrame:
    """
    Nettoyage du dataset.
    """

    dataset = dataset.copy()

    dataset.dropna(inplace=True)

    dataset.reset_index(drop=True, inplace=True)

    return dataset


# ------------------------------------------------------------------
# Encodage
# ------------------------------------------------------------------

def encode_origin(dataset: pd.DataFrame) -> pd.DataFrame:
    """
    Transforme Origin en variables One-Hot.
    """

    dataset = dataset.copy()

    dataset["Origin"] = dataset["Origin"].map(
        ORIGIN_MAPPING
    )

    dataset = pd.get_dummies(
        dataset,
        columns=["Origin"],
        prefix="",
        prefix_sep="",
        dtype=float,
    )

    # Garantit la présence des 3 colonnes
    for column in ["USA", "Europe", "Japan"]:
        if column not in dataset.columns:
            dataset[column] = 0.0

    dataset = dataset.reindex(
        columns=[
            "MPG",
            "Cylinders",
            "Displacement",
            "Horsepower",
            "Weight",
            "Acceleration",
            "Model Year",
            "USA",
            "Europe",
            "Japan",
        ]
    )

    return dataset


# ------------------------------------------------------------------
# Séparation Features / Labels
# ------------------------------------------------------------------

def split_features_labels(
    dataset: pd.DataFrame,
):

    features = dataset.copy()

    labels = features.pop("MPG")

    return features, labels


# ------------------------------------------------------------------
# Train/Test Split
# ------------------------------------------------------------------

def split_train_test(
    features,
    labels,
):

    return train_test_split(
        features,
        labels,
        test_size=0.20,
        random_state=42,
    )


# ------------------------------------------------------------------
# Normalizer TensorFlow
# ------------------------------------------------------------------

def build_normalizer(
    train_features,
):

    normalizer = tf.keras.layers.Normalization(
        axis=-1
    )

    normalizer.adapt(
        np.array(train_features)
    )

    return normalizer


# ------------------------------------------------------------------
# Pipeline complet
# ------------------------------------------------------------------

def prepare_data():
    """
    Pipeline complet de préparation.
    """

    dataset = load_dataset()

    dataset = clean_dataset(dataset)

    dataset = encode_origin(dataset)

    features, labels = split_features_labels(
        dataset
    )

    (
        train_features,
        test_features,
        train_labels,
        test_labels,
    ) = split_train_test(
        features,
        labels,
    )

    normalizer = build_normalizer(
        train_features
    )
    
    print("\nColonnes utilisées :")
    print(train_features.columns.tolist())

    print("\nShape :", train_features.shape)

    return (
        train_features,
        test_features,
        train_labels,
        test_labels,
        normalizer,
    )
