from ultralytics import YOLO
from config.settings import MODEL_PATH

def cargar_modelo():
    """
    Carga el modelo YOLO configurado en settings.
    """
    return YOLO(MODEL_PATH)