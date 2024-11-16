from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, JSONResponse

# Datos de ejemplo
data = [
    {"INGMEN": 1000000, "ESTSOC": 1, "COSMEN": 50000, "PRIORIDAD": 1},
    {"INGMEN": 1500000, "ESTSOC": 2, "COSMEN": 60000, "PRIORIDAD": 1},
    {"INGMEN": 2000000, "ESTSOC": 3, "COSMEN": 70000, "PRIORIDAD": 1},
    {"INGMEN": 1800000, "ESTSOC": 2, "COSMEN": 55000, "PRIORIDAD": 1},
    {"INGMEN": 1200000, "ESTSOC": 1, "COSMEN": 65000, "PRIORIDAD": 1},
    {"INGMEN": 2500000, "ESTSOC": 3, "COSMEN": 80000, "PRIORIDAD": 1},
    {"INGMEN": 2800000, "ESTSOC": 1, "COSMEN": 50000, "PRIORIDAD": 1},
    {"INGMEN": 2200000, "ESTSOC": 2, "COSMEN": 60000, "PRIORIDAD": 1},
    {"INGMEN": 1500000, "ESTSOC": 3, "COSMEN": 90000, "PRIORIDAD": 1},
    {"INGMEN": 2000000, "ESTSOC": 1, "COSMEN": 75000, "PRIORIDAD": 1},
    {"INGMEN": 3500000, "ESTSOC": 1, "COSMEN": 50000, "PRIORIDAD": 0},
    {"INGMEN": 4000000, "ESTSOC": 2, "COSMEN": 60000, "PRIORIDAD": 0},
    {"INGMEN": 4500000, "ESTSOC": 3, "COSMEN": 45000, "PRIORIDAD": 0},
    {"INGMEN": 2000000, "ESTSOC": 4, "COSMEN": 50000, "PRIORIDAD": 0},
    {"INGMEN": 2500000, "ESTSOC": 5, "COSMEN": 60000, "PRIORIDAD": 0},
    {"INGMEN": 3000000, "ESTSOC": 6, "COSMEN": 45000, "PRIORIDAD": 0},
    {"INGMEN": 1000000, "ESTSOC": 1, "COSMEN": 30000, "PRIORIDAD": 0},
    {"INGMEN": 2000000, "ESTSOC": 2, "COSMEN": 20000, "PRIORIDAD": 0},
    {"INGMEN": 1500000, "ESTSOC": 3, "COSMEN": 35000, "PRIORIDAD": 0},
    {"INGMEN": 3200000, "ESTSOC": 1, "COSMEN": 55000, "PRIORIDAD": 0},
]

# Separar características y etiquetas
X = [[item["INGMEN"], item["ESTSOC"], item["COSMEN"]] for item in data]
y = [item["PRIORIDAD"] for item in data]

# Dividir datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el clasificador Random Forest
rf = RandomForestClassifier(class_weight='balanced', random_state=42)

# Entrenar el clasificador
rf.fit(X_train, y_train)

# Evaluar el modelo
y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Precisión:", accuracy)

# FastAPI
app = FastAPI()
app.title = "Identificación de Hogares Vulnerables para Energías Limpias"
app.version = "1.0.0"

@app.get("/", tags=["Home"])
def home():
    return HTMLResponse("<h1>¡Bienvenido a nuestra aplicación de priorización de viviendas para energías limpias!</h1>")

@app.get("/simulador", tags=["Simulador"])
def get_simulador(Ingresos: int = Query(...), Estrato: int = Query(...), Costo: int = Query(...)):
    new_data = [[Ingresos, Estrato, Costo]]
    prediction = rf.predict(new_data)
    prediction_label = "Sí priorizado" if prediction[0] == 1 else "No priorizado"
    return JSONResponse(content={"Predicción de Priorización": prediction_label})
