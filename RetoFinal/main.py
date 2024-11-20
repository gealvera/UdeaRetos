from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

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

app.mount("/images", StaticFiles(directory="images"), name="images")

@app.get("/", tags=["Home"])
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simulador de Prioización de Acceso a Energías Limpias</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                text-align: center;
                background-image: url('/images/energia.png');
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                color: #fff;
            }
            form {
                display: inline-block;
                margin-top: 50px;
                padding: 20px;
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
                color: #000;
            }
            input {
                margin: 10px 0;
                padding: 10px;
                width: 300px;
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            label {
                display: block;
                margin-top: 10px;
                font-weight: bold;
                text-align: left;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                color: white;
                background-color: #28a745;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                margin-top: 20px;
            }
            button:hover {
                background-color: #218838;
            }
            #resultado {
                margin-top: 20px;
                padding: 15px;
                font-size: 18px;
                font-weight: bold;
                color: white;
                border-radius: 5px;
                display: inline-block;
                width: 50%;
                max-width: 400px;
            }
            #resultado.si {
                background-color: #28a745;
                border: 2px solid #218838;
            }
            #resultado.no {
                background-color: #dc3545;
                border: 2px solid #c82333;
            }
        </style>
    </head>
    <body>
        <h1>Simulador de Priorización de Acceso a Energías Limpias</h1>
        <form onsubmit="simulate(event)">
            <label for="ingresos">Ingresos Mensuales:</label>
            <input type="number" id="ingresos" placeholder="Ingresos" required /><br />

            <label for="estrato">Estrato Socioeconómico:</label>
            <input type="number" id="estrato" placeholder="Estrato" required /><br />

            <label for="costo">Costo Energía Mensual:</label>
            <input type="number" id="costo" placeholder="Costo Energía" required /><br />

            <button type="submit">Simular</button>
        </form>
        <div id="resultado-container" style="margin-top: 20px; display: none;">
            <p id="resultado"></p>
        </div>
        <script>
            async function simulate(event) {
                event.preventDefault();
                const ingresos = document.getElementById('ingresos').value;
                const estrato = document.getElementById('estrato').value;
                const costo = document.getElementById('costo').value;

                // Llamar al endpoint de simulación
                const response = await fetch(`/simulador?Ingresos=${parseInt(ingresos)}&Estrato=${parseInt(estrato)}&Costo=${parseInt(costo)}`);
                const result = await response.json();

                // Mostrar el resultado con estilo
                const resultado = document.getElementById("resultado");
                const resultadoContainer = document.getElementById("resultado-container");
                resultadoContainer.style.display = "block";
                resultado.innerText = result["Predicción de Priorización"];

                // Estilo del resultado
                if (result["Predicción de Priorización"] === "Sí Priorizado") {
                    resultado.className = "si";
                } else {
                    resultado.className = "no";
                }
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/simulador", tags=["Simulador"])
def get_simulador(Ingresos: int = Query(...), Estrato: int = Query(...), Costo: int = Query(...)):
    new_data = [[Ingresos, Estrato, Costo]]
    prediction = rf.predict(new_data)
    prediction_label = "Sí Priorizado" if prediction[0] == 1 else "No Priorizado"
    return JSONResponse(content={"Predicción de Priorización": prediction_label})
