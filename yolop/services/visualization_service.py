import cv2
from config.settings import WINDOW_NAME

def dibujar_conteo(results, frame, conteo):
    """
    Dibuja bounding boxes y conteo.
    """
    annotated = results[0].plot()

    y = 30
    for obj, cantidad in conteo.items():
        cv2.putText(
            annotated,
            f"{obj}: {cantidad}",
            (10, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )
        y += 25

    return annotated


def mostrar_frame(frame):
    """
    Muestra el frame en pantalla.
    """
    cv2.imshow(WINDOW_NAME, frame)