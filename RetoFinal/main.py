from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction import DictVectorizer
from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse

# 1: PRIORIZADO, 0: NO PRIORIZADO
data = [
    {"INGMEN": 1000000, "ESTSOC": 1, "COSMEN": 10000, "PRIORIDAD": 0},
    {"INGMEN": 1000000, "ESTSOC": 1, "COSMEN": 20000, "PRIORIDAD": 0},
    {"INGMEN": 1000000, "ESTSOC": 1, "COSMEN": 30000, "PRIORIDAD": 0},
    {"INGMEN": 1000000, "ESTSOC": 1, "COSMEN": 40000, "PRIORIDAD": 1},
    {"INGMEN": 1000000, "ESTSOC": 1, "COSMEN": 50000, "PRIORIDAD": 1},
    {"INGMEN": 1000000, "ESTSOC": 1, "COSMEN": 60000, "PRIORIDAD": 1},
    {"INGMEN": 1000000, "ESTSOC": 1, "COSMEN": 70000, "PRIORIDAD": 1},
    {"INGMEN": 1000000, "ESTSOC": 1, "COSMEN": 80000, "PRIORIDAD": 1},
    {"INGMEN": 1000000, "ESTSOC": 1, "COSMEN": 90000, "PRIORIDAD": 1},
    {"INGMEN": 1000000, "ESTSOC": 2, "COSMEN": 50000, "PRIORIDAD": 1},
    {"INGMEN": 1000000, "ESTSOC": 2, "COSMEN": 60000, "PRIORIDAD": 0},
    {"INGMEN": 1000000, "ESTSOC": 2, "COSMEN": 70000, "PRIORIDAD": 0},
    {"INGMEN": 1000000, "ESTSOC": 2, "COSMEN": 80000, "PRIORIDAD": 1},
    {"INGMEN": 1000000, "ESTSOC": 2, "COSMEN": 90000, "PRIORIDAD": 1},
    {"INGMEN": 2000000, "ESTSOC": 3, "COSMEN": 50000, "PRIORIDAD": 0}
]

# Lista de variables
X = [{k: v for k, v in item.items() if k != "PRIORIDAD"} for item in data] 
y = [item["PRIORIDAD"] for item in data]

# Vectorizamos la X en un arreglo 2D
vectorizer = DictVectorizer(sparse=False)
X_vectorized = vectorizer.fit_transform(X) 

X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Crear el clasificador de vecinos mas cercanos
knn = KNeighborsClassifier(n_neighbors=3)

# Entrenar el clasificador
knn.fit(X_train, y_train)

# Predecir las etiquetas para los datos de prueba
y_pred = knn.predict(X_test)

# Calcular la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)

print("Precisión:", accuracy)

# Crea una instancia de FastAPI
app = FastAPI()
app.title = "Identificación de Hogares Vulnerables para la priorización de acceso a energías limpias"
app.version = "1.0.0"

# Definie una ruta para la API
@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>¡Bienvenido a nuestra aplicación!!!</h1>')

@app.get('/datosviviendas', tags=['Datos Viviendas'])
def get_datos_viviendas():
    if not data:
        raise HTTPException(status_code=500, detail="NO hay datos disponibles.")
    return data

@app.get('/simulador', tags=['Simulador'])
def get_simulador(Ingresos: int, Estrato: int, Costo: int):
    new_data = {"INGMEN": Ingresos, "ESTSOC": Estrato, "COSMEN": Costo}
    data_vectorized_test = vectorizer.transform([new_data])
    prediction = knn.predict(data_vectorized_test)

    # Convertir la predicción en un formato adecuado para JSON
    prediction_label = "Si priorizado" if prediction[0] == 1 else "No priorizado"

    return JSONResponse(content={"Predicción de Priorización": prediction_label})


