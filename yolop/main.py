from models.model_loader import cargar_modelo
from utils.camera import iniciar_camara
from services.detection_service import detectar_objetos
from services.counting_service import contar_objetos
from services.visualization_service import dibujar_conteo, mostrar_frame

def main():
    model = cargar_modelo()
    cap = iniciar_camara()

    print("Iniciando detección... (ESC para salir)")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = detectar_objetos(model, frame)
        conteo = contar_objetos(results, model.names)

        frame = dibujar_conteo(results, frame, conteo)
        mostrar_frame(frame)

        if salir():
            break

    cap.release()


def salir():
    import cv2
    return cv2.waitKey(1) & 0xFF == 27


if __name__ == "__main__":
    main()