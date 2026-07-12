#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from ml.predictor import predictor
from ml.schemas import CarFeatures

from ml.exceptions import PredictionError

from .forms import PredictionForm


def home(request):
    """
    Affiche le formulaire et réalise une prédiction.
    """

    prediction = None

    if request.method == "POST":

        form = PredictionForm(request.POST)

        if form.is_valid():

            car = CarFeatures(
                cylinders=form.cleaned_data["cylinders"],
                displacement=form.cleaned_data["displacement"],
                horsepower=form.cleaned_data["horsepower"],
                weight=form.cleaned_data["weight"],
                acceleration=form.cleaned_data["acceleration"],
                model_year=form.cleaned_data["model_year"],
                origin=form.cleaned_data["origin"],
            )
            try:
                prediction = predictor.predict(car)
            except PredictionError as e:
                form.add_error(None, str(e))

    else:

        form = PredictionForm()

    context = {
        "form": form,
        "prediction": prediction,
    }

    return render(
        request,
        "predictor/home.html",
        context,
    )
