import cv2
import numpy as np


# Cargar la imagen en color
color_image = cv2.imread('Pictures/Miya.jpeg')

# Cargar la misma imagen en escala de grises
gray_image = cv2.imread('Pictures/Miya.jpeg', cv2.IMREAD_GRAYSCALE)

# Mostrar la imagen en color
cv2.imshow('Miya - Color', color_image)

# Mostrar la imagen en escala de grises
cv2.imshow('Miya - Escala de Grises', gray_image)

# Esperar a que se presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

# Cargar la imagen original
original_image = cv2.imread('Pictures/Miya.jpeg')

# Rotar la imagen 90 grados en sentido horario
(h, w) = original_image.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, -90, 1.0)  # Ángulo negativo para rotar en sentido horario
rotated_image = cv2.warpAffine(original_image, rotation_matrix, (w, h))

# Escalar la imagen al doble de su tamaño original
scaled_image = cv2.resize(original_image, (w * 2, h * 2))

# Mostrar la imagen rotada
cv2.imshow('Imagen Rotada 90°', rotated_image)

# Mostrar la imagen escalada
cv2.imshow('Imagen Escalada al Doble', scaled_image)

# Esperar a que se presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

# Cargar la imagen en escala de grises
gray_image = cv2.imread('Pictures/Miya.jpeg', cv2.IMREAD_GRAYSCALE)

# Aplicar un filtro gaussiano para suavizar la imagen
gaussian_blur = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Aplicar un filtro de realce para mejorar los detalles
kernel = np.array([[-1, -1, -1],
                   [-1,  9, -1],
                   [-1, -1, -1]])
sharpened_image = cv2.filter2D(original_image, -1, kernel)

# Mostrar la imagen suavizada
cv2.imshow('Imagen Suavizada (Filtro Gaussiano)', gaussian_blur)

# Mostrar la imagen realzada
cv2.imshow('Imagen Realzada (Filtro de Afilado)', sharpened_image)

# Esperar a que se presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()

#Detección de bordes
# Cargar la imagen en escala de grises 
image = cv2.imread('Pictures/Miya.jpeg', cv2.IMREAD_GRAYSCALE)

# Aplicar el operador Sobel para detectar los bordes
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

#Combinar las respuestas en magnitud
edges = cv2.magnitude(sobelx, sobely) 

#Normalizar los valores para mostrar la imagen correctamente
edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

#Mostrar la imagen con los bordes detectados
cv2.imshow('Miya', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

