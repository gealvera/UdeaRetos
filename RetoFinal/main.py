from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
import pandas as pd

# Historial de resultados simulados
historial_simulaciones = []

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

# Datos de ejemplo para energía limpia
data_energia = [
    {"RADSOL": 6.5, "VELVIE": 12.0, "ENERGIA": "Solar"},
    {"RADSOL": 5.0, "VELVIE": 15.0, "ENERGIA": "Eólica"},
    {"RADSOL": 7.0, "VELVIE": 8.0, "ENERGIA": "Solar"},
    {"RADSOL": 3.5, "VELVIE": 20.0, "ENERGIA": "Eólica"}
]

# Separar características y etiquetas
X = [[item["INGMEN"], item["ESTSOC"], item["COSMEN"]] for item in data]
y = [item["PRIORIDAD"] for item in data]

# Dividir datos y entrenar RandomForestClassifier para clasificación de prioridad
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rf = RandomForestClassifier(class_weight='balanced', random_state=42)
rf.fit(X_train, y_train)

# Preparar datos para el modelo de energía limpia
X_energia = [[item["RADSOL"], item["VELVIE"]] for item in data_energia]
y_energia = [1 if item["ENERGIA"] == "Solar" else 0 for item in data_energia]  # 1: Solar, 0: Eólica

# Dividir datos y entrenar RandomForestClassifier para energía limpia
X_train_ene, X_test_ene, y_train_ene, y_test_ene = train_test_split(X_energia, y_energia, test_size=0.2, random_state=42)
rf_energia = RandomForestClassifier(class_weight='balanced', random_state=42)
rf_energia.fit(X_train_ene, y_train_ene)

# Evaluar el modelo
y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Precisión Priorización:", accuracy)
# Evaluar el modelo
y_pred_energia = rf_energia.predict(X_test_ene)
accuracy = accuracy_score(y_test_ene, y_pred_energia)
print("Precisión Energía:", accuracy)

# FastAPI
app = FastAPI()
app.title = "Identificación de Hogares Vulnerables para Energías Limpias"
app.version = "1.0.0"

app.mount("/images", StaticFiles(directory="images"), name="images")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura el directorio de plantillas
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse, tags=["Home"])
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/simulador", tags=["Simulador"])
def get_simulador(Ingresos: int = Query(...), Estrato: int = Query(...), Costo: int = Query(...)):
    new_data = [[Ingresos, Estrato, Costo]]
    prediction = rf.predict(new_data)
    prediction_label = "Sí Priorizado" if prediction[0] == 1 else "No Priorizado"

    # Guardar en el historial
    resultado = {
        "Ingresos": Ingresos,
        "Estrato": Estrato,
        "Costo": Costo,
        "Prioridad": prediction_label,
    }
    historial_simulaciones.append(resultado)

    return JSONResponse(content={"Predicción de Priorización": prediction_label})

@app.get("/energia", tags=["Energía Limpia"])
def get_energia(Radiacion: float = Query(...), Viento: float = Query(...)):
    new_data = [[Radiacion, Viento]]
    prediction = rf_energia.predict(new_data)
    prediction_label = "Solar" if prediction[0] == 1 else "Eólica"

    # Guardar en el historial
    resultado = {
        "Radiación": Radiacion,
        "Velocidad Viento": Viento,
        "Energía Recomendada": prediction_label,
    }
    # Modificar el último registro del historial
    if historial_simulaciones:  
        historial_simulaciones[-1].update({
            "Radiación": Radiacion,
            "Velocidad Viento": Viento,
            "Energía Recomendada": prediction_label,
        })

    return JSONResponse(content={"Energía Recomendada": prediction_label})

@app.get("/exportar", tags=["Exportar"])
def exportar_datos():
    if not historial_simulaciones:
        return JSONResponse(
            content={"error": "No hay resultados para exportar."}, status_code=400
        )

    # Crear un DataFrame de pandas con el historial
    df = pd.DataFrame(historial_simulaciones)

    # Definir el archivo temporal para guardar el Excel
    excel_path = "historial_resultados.xlsx"

    # Guardar el DataFrame como archivo Excel
    df.to_excel(excel_path, index=False, engine="openpyxl")

    # Devolver el archivo como respuesta
    return FileResponse(
        path=excel_path,
        filename="historial_resultados.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )