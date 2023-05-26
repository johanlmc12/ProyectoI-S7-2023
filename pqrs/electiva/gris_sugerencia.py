import cv2



def convertir_a_grises(imagen):
    imagen_original = cv2.imread(imagen)

    if imagen_original is None:
        print("No se pudo cargar la imagen")
        return

    # Convertir la imagen a escala de grises
    imagen_grises = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("sugerencia_escala.jpg", imagen_grises)

    return imagen_grises

ruta_imagen = 'sugerencias.jpg'
imagen_gris1 = convertir_a_grises(ruta_imagen)