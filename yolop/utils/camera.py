import cv2
from config.settings import CAMERA_INDEX

def iniciar_camara():
    """
    Inicializa la cámara.
    """
    cap = cv2.VideoCapture(CAMERA_INDEX)

    if not cap.isOpened():
        raise RuntimeError("No se pudo abrir la cámara.")

    return cap