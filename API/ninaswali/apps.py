import os
import joblib
from django.apps import AppConfig
from django.conf import settings


class NinaswaliConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ninaswali'
    MODEL_FILE = os.path.join(settings.MODELS, "modelNameHere")
    model = joblib.load(MODEL_FILE)
