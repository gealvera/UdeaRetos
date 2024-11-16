import nltk
from nltk.tokenize import word_tokenize #Divide el texto en palabras
from nltk.corpus import stopwords #Lista de palabras comunes
from nltk.probability import FreqDist #Frecuencia de palabras
from collections import Counter #Frecuencia de palabras

texto = """ ¿Cómo funciona el sistema de priorización de hogares para energías limpias que permitan la priorización de planes de energías?"""

# Tokenizar el texto
palabras = word_tokenize(texto, language="spanish")
print(palabras)

# Stopwords = eliminar los conectores
stopwords = set(stopwords.words("spanish"))

# Filtrar las palabras que estan en la lista de stopwords
palabras_filtradas = [palabra for palabra in palabras if palabra not in stopwords]
print(palabras_filtradas)

# Frecuencia de palabras
frecuencia = FreqDist(palabras_filtradas)
print(frecuencia.most_common(4))