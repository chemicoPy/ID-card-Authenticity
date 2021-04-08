from django.apps import AppConfig
import html
from pathlib import Path
from .National_ID_card_genuineness import check_image_similarity


class MainConfig(AppConfig):
    name = "main"
    name = "main"
    predictor = check_image_similarity
