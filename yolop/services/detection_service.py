def detectar_objetos(model, frame):
    """
    Ejecuta la inferencia del modelo YOLO.

    Args:
        model: Modelo YOLO cargado
        frame: Imagen actual

    Returns:
        results: Resultados de detección
    """
    return model(frame)