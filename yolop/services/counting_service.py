def contar_objetos(results, names):
    """
    Cuenta los objetos detectados.

    Args:
        results: Resultado de YOLO
        names: Diccionario de clases

    Returns:
        dict: Conteo de objetos
    """
    conteo = {}

    for r in results:
        for box in r.boxes:
            clase = int(box.cls)
            nombre = names[clase]

            conteo[nombre] = conteo.get(nombre, 0) + 1

    return conteo