import cv2
import numpy as np

#cargamos imagen
image = cv2.imread('Pictures/Rio.jpg')
image2 = cv2.imread('Pictures/Nevado.jpg')
image3 = cv2.imread('Pictures/Montanas.jpg')

cv2.imshow('Rio', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#obtener dimensiones de la imagen
hight, width = image.shape[:2]
center = (width/2, hight/2)

#rotar la imagen
angulo = 90
matrix = cv2.getRotationMatrix2D(center, angulo, 1.0)
rotated = cv2.warpAffine(image2, matrix, (width, hight))

cv2.imshow('Nevado', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Definir la matriz de traslación
tx, ty = 100, 50 
M = np.float32([[1, 0, tx], [0, 1, ty]])

#Aplicar la matriz de traslación a la imagen
translated = cv2.warpAffine(image3, M, (image3.shape[1], image.shape[0]))

#Mostratre la imagen trasladada
cv2.imshow('Montana', translated)
cv2.waitKey(0)
cv2.destroyAllWindows() 

#Escala
# Definir la nueva altura y ancho de la imagen
new_height, new_width = 300, 250

#Aplicar la escala de la imagen
scaled = cv2.resize(image, (new_width, new_height))

#Mostrar la imagen escalada
cv2.imshow('Rio', scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Recorte
# Definir las coordenadas del área de interés ROI 
x, y, w, h = 100, 100, 200, 150

#Recortar la región de interés ROI
cropped = image2[y:y+h, x:x+w] 

#Mostrar la imagen recortada
cv2.imshow('Nevado', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Suavizado
# Aplicar el filtro Gaussiano para suavisar la imagen 
smoothed = cv2.GaussianBlur(image, (5, 5), 0)

#Mostrar la imagen suavisada
cv2.imshow('Rio', smoothed)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Realce
# Definir el kernel para el filtro de afilado
kernel = np.array([[-1, -1, -1], 
                   [-1, 9, -1], 
                   [-1, -1, -1]])

#Aplicar el filtro de afilado para realzar los detalles
sharpened = cv2.filter2D(image3, -1, kernel)

#Mostrar la imagen realzada
cv2.imshow('Montana', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Detección de bordes
# Cargar la imagen en escala de grises 
image = cv2.imread('Pictures/Rio.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar el operador Sobel para detectar los bordes
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

#Combinar las respuestas en magnitud
edges = cv2.magnitude(sobelx, sobely) 

#Normalizar los valores para mostrar la imagen correctamente
edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

#Mostrar la imagen con los bordes detectados
cv2.imshow('Rio', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()