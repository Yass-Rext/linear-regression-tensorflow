"""
Exceptions personnalisées du module ML.
"""


class PredictionError(Exception):
    """Erreur générale de prédiction."""


class InvalidOriginError(PredictionError):
    """Origine inconnue."""


class ModelNotLoadedError(PredictionError):
    """Le modèle TensorFlow est introuvable ou impossible à charger."""
