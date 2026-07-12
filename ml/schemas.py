"""
Objets métiers utilisés par le module Machine Learning.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class CarFeatures:
    """
    Représente les caractéristiques d'une voiture.
    """

    cylinders: int
    displacement: float
    horsepower: float
    weight: float
    acceleration: float
    model_year: int
    origin: str
