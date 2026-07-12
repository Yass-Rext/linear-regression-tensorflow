from pathlib import Path
import pickle

import pandas as pd
import tensorflow as tf

from .exceptions import (
    InvalidOriginError,
    ModelNotLoadedError,
)

from .schemas import CarFeatures
    

BASE_DIR = Path(__file__).parent

MODEL_DIR = BASE_DIR / "saved_models"

MODEL_PATH = MODEL_DIR / "model.keras"

FEATURE_COLUMNS_PATH = MODEL_DIR / "feature_columns.pkl"


class RegressionPredictor:

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

        self.model = None

        self.feature_columns = None

    def _load(self):

        if self.model is None:

            if not MODEL_PATH.exists():

                raise ModelNotLoadedError(
                    f"Le modèle est introuvable : {MODEL_PATH}"
                )

            self.model = tf.keras.models.load_model(
                MODEL_PATH
            )

        if self.feature_columns is None:

            if not FEATURE_COLUMNS_PATH.exists():

                raise ModelNotLoadedError(
                    f"Le fichier des colonnes est introuvable : {FEATURE_COLUMNS_PATH}"
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

        if car.origin not in self.VALID_ORIGINS:

            raise InvalidOriginError(
                f"Origine invalide : {car.origin}"
            )

        sample = {
            column: 0.0
            for column in self.feature_columns
        }

        for column, attribute in self.NUMERIC_MAPPING.items():

            sample[column] = float(
                getattr(car, attribute)
            )

        sample[car.origin] = 1.0

        df = pd.DataFrame([sample])

        df = df[self.feature_columns]

        return df

    def predict(
        self,
        car: CarFeatures,
    ) -> float:

        self._load()

        prediction = self.model.predict(
            self._prepare_input(car),
            verbose=0,
        )

        return float(prediction[0][0])


predictor = RegressionPredictor()