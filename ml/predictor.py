"""
Service de prédiction TensorFlow.
"""

from pathlib import Path
import pickle

import pandas as pd
import tensorflow as tf

from .exceptions import InvalidOriginError
from .schemas import CarFeatures


BASE_DIR = Path(__file__).parent

MODEL_DIR = BASE_DIR / "saved_models"

MODEL_PATH = MODEL_DIR / "model.keras"

FEATURE_COLUMNS_PATH = MODEL_DIR / "feature_columns.pkl"


class RegressionPredictor:
    """
    Service de prédiction.
    """

    VALID_ORIGINS = (
        "USA",
        "Europe",
        "Japan",
    )

    NUMERIC_MAPPING = {
        "Cylinders": "cylinders",
        "Displacement": "displacement",
        "Horsepower": "horsepower",
        "Weight": "weight",
        "Acceleration": "acceleration",
        "Model Year": "model_year",
    }

    def __init__(self):

        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Le modèle est introuvable : {MODEL_PATH}"
            )

        if not FEATURE_COLUMNS_PATH.exists():
            raise FileNotFoundError(
                f"Le fichier des colonnes est introuvable : {FEATURE_COLUMNS_PATH}"
            )

        self.model = tf.keras.models.load_model(
            MODEL_PATH
        )

        with open(
            FEATURE_COLUMNS_PATH,
            "rb",
        ) as file:

            self.feature_columns = pickle.load(file)

    def _prepare_input(
        self,
        car: CarFeatures,
    ) -> pd.DataFrame:
        """
        Prépare les données pour TensorFlow.
        """

        if car.origin not in self.VALID_ORIGINS:
            raise InvalidOriginError(
                f"Origine invalide : {car.origin}"
            )

        sample = {
            column: 0
            for column in self.feature_columns
        }

        for column, attribute in self.NUMERIC_MAPPING.items():
            sample[column] = getattr(
                car,
                attribute,
            )

        sample[car.origin] = 1

        return pd.DataFrame([sample])

    def predict(
        self,
        car: CarFeatures,
    ) -> float:
        """
        Effectue une prédiction.
        """

        sample = self._prepare_input(
            car
        )

        prediction = self.model.predict(
            sample,
            verbose=0,
        )

        return float(
            prediction[0][0]
        )


predictor = RegressionPredictor()
