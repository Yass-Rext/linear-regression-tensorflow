from django import forms


class PredictionForm(forms.Form):

    ORIGIN_CHOICES = [
        ("USA", "USA"),
        ("Europe", "Europe"),
        ("Japan", "Japan"),
    ]

    cylinders = forms.IntegerField(
        label="Nombre de cylindres",
        min_value=1,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    displacement = forms.FloatField(
        label="Cylindrée",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    horsepower = forms.FloatField(
    label="Puissance",
    widget=forms.NumberInput(
        attrs={
            "class": "form-control",
            "step": "0.1",
            "placeholder": "Ex : 130",
        }
    ),
   )

    weight = forms.FloatField(
        label="Poids",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    acceleration = forms.FloatField(
        label="Accélération",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    model_year = forms.IntegerField(
        label="Année du modèle",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    origin = forms.ChoiceField(
        label="Origine",
        choices=ORIGIN_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
    )
