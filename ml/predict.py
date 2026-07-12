from pathlib import Path
import pickle

import pandas as pd
import tensorflow as tf


BASE_DIR = Path(__file__).parent
MODEL_DIR = BASE_DIR / "saved_models"

MODEL_PATH = MODEL_DIR / "model.keras"
FEATURES_PATH = MODEL_DIR / "feature_columns.pkl"


MODEL = tf.keras.models.load_model(MODEL_PATH)

with open(FEATURES_PATH, "rb") as file:
    FEATURE_COLUMNS = pickle.load(file)


NUMERIC_COLUMNS = [
    "Cylinders",
    "Displacement",
    "Horsepower",
    "Weight",
    "Acceleration",
    "Model Year",
]


def prepare_input(data: dict) -> pd.DataFrame:
    sample = {column: 0 for column in FEATURE_COLUMNS}

    for column in NUMERIC_COLUMNS:
        sample[column] = float(data[column])

    origin = data["Origin"]
    sample[origin] = 1

    return pd.DataFrame([sample])


def predict(data: dict) -> float:
    sample = prepare_input(data)
    prediction = MODEL.predict(sample, verbose=0)
    return float(prediction[0][0])
