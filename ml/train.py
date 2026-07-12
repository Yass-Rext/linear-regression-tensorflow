"""
Entraînement du modèle de régression linéaire TensorFlow.

Ce script :

- prépare les données
- construit le modèle
- entraîne le modèle
- l'évalue
- sauvegarde le modèle
- sauvegarde les colonnes des variables
"""

from pathlib import Path
import pickle

import tensorflow as tf
from tensorflow.keras import layers

from .preprocessing import prepare_data


# ------------------------------------------------------------------
# Répertoires
# ------------------------------------------------------------------

BASE_DIR = Path(__file__).parent

MODEL_DIR = BASE_DIR / "saved_models"

MODEL_DIR.mkdir(exist_ok=True)

MODEL_PATH = MODEL_DIR / "model.keras"

FEATURE_COLUMNS_PATH = MODEL_DIR / "feature_columns.pkl"


# ------------------------------------------------------------------
# Construction du modèle
# ------------------------------------------------------------------

def build_model(normalizer):
    """
    Construit un modèle de régression linéaire.
    """

    model = tf.keras.Sequential(
        [
            normalizer,
            layers.Dense(
                units=1,
            ),
        ]
    )

    return model


# ------------------------------------------------------------------
# Compilation
# ------------------------------------------------------------------

def compile_model(model):
    """
    Compile le modèle.
    """

    model.compile(
        optimizer=tf.keras.optimizers.Adam(
            learning_rate=0.1,
        ),
        loss="mean_absolute_error",
        metrics=[
            "mae",
        ],
    )


# ------------------------------------------------------------------
# Entraînement
# ------------------------------------------------------------------

def train_model(
    model,
    train_features,
    train_labels,
):
    """
    Entraîne le modèle.
    """

    history = model.fit(
        train_features,
        train_labels,
        validation_split=0.2,
        epochs=100,
        verbose=1,
    )

    return history


# ------------------------------------------------------------------
# Evaluation
# ------------------------------------------------------------------

def evaluate_model(
    model,
    test_features,
    test_labels,
):
    """
    Evalue le modèle.
    """

    loss, mae = model.evaluate(
        test_features,
        test_labels,
        verbose=0,
    )

    print("\n" + "=" * 50)

    print(f"Test Loss : {loss:.3f}")

    print(f"Test MAE  : {mae:.3f}")

    print("=" * 50)


# ------------------------------------------------------------------
# Sauvegarde du modèle
# ------------------------------------------------------------------

def save_model(model):
    """
    Sauvegarde le modèle TensorFlow.
    """

    model.save(MODEL_PATH)

    print()

    print(f"Modèle sauvegardé : {MODEL_PATH}")


# ------------------------------------------------------------------
# Sauvegarde des colonnes
# ------------------------------------------------------------------

def save_feature_columns(train_features):
    """
    Sauvegarde l'ordre des colonnes.
    """

    with open(
        FEATURE_COLUMNS_PATH,
        "wb",
    ) as file:

        pickle.dump(
            list(train_features.columns),
            file,
        )

    print(
        f"Colonnes sauvegardées : {FEATURE_COLUMNS_PATH}"
    )


# ------------------------------------------------------------------
# Pipeline complet
# ------------------------------------------------------------------

def main():

    (
        train_features,
        test_features,
        train_labels,
        test_labels,
        normalizer,
    ) = prepare_data()

    print()

    print("Construction du modèle...")

    model = build_model(normalizer)

    compile_model(model)

    print()

    print("Début de l'entraînement...\n")

    train_model(
        model,
        train_features,
        train_labels,
    )

    print()

    print("Evaluation du modèle...")

    evaluate_model(
        model,
        test_features,
        test_labels,
    )

    print()

    print("Sauvegarde du modèle...")

    save_model(model)

    save_feature_columns(
        train_features,
    )

    print()

    print("Entraînement terminé avec succès.")


# ------------------------------------------------------------------

if __name__ == "__main__":
    main()
