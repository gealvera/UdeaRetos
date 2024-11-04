
# Análisis del Notebook ZNI Energy

## 1. Descripción General
El notebook ZNI Energy analiza el **consumo energético** en las Zonas No Interconectadas (ZNI) de Colombia. Su objetivo es identificar patrones de consumo, priorizar zonas para proyectos energéticos, predecir la demanda futura y explorar el potencial de energías renovables como la **solar** y **eólica**.

## 2. Datasets Usados
### 2.1. Energia_en_ZNI.csv
- **Origen**: IPSE (Instituto de Planificación y Promoción de Soluciones Energéticas).
- **Variables Clave**:
  - **PROVINCE, CITY, ZONE**: Ubicación geográfica de los registros.
  - **ACTIVE_POWER, REACTIVE_POWER, MAX_POWER**: Consumo y demanda energética.
  - **DAILY_MEAN_HOURS**: Horas de servicio promedio diario.
- **Observaciones**:
  - El dataset abarca desde enero 2020 hasta junio 2023.
  - **Inconsistencias**: Zonas con valores cero en energía reactiva y horas de servicio.

### 2.2. Colombia Solar Atlas 2019
- **Origen**: Global Solar Atlas.
- **Variables Clave**:
  - **PVOUT, GHI**: Potencial fotovoltaico e irradiación solar.
  - **TEMP**: Temperatura del aire en °C.
- **Formato**: Archivos GeoTIFF con resolución espacial variable.

### 2.3. Colombia Wind Atlas of Power Density
- **Origen**: Global Wind Atlas.
- **Variables Clave**:
  - **Velocidad del Viento, Densidad de Potencia**: Medidos a diferentes alturas.
- **Formato**: Archivos GeoTIFF.

## 3. Análisis Realizado
- **Exploratory Data Analysis (EDA)**:
  - Comparaciones de consumo energético entre zonas y ciudades.
  - Análisis del factor de potencia y horas de servicio.
- **Modelos ARMA y ARIMA**:
  - Predicción de demanda energética a partir de series temporales.
  - Estimación del consumo futuro para planificar proyectos energéticos.

## 4. Resultados y Visualizaciones
- **Visualización del EDA**:
  - Gráficos de barras para comparar consumo entre zonas.
  - Gráficos de pastel que muestran distribución de horas de servicio.
- **Resultados de Predicción**:
  - Gráficos que muestran la demanda proyectada comparada con datos históricos.
- **Potencial de Energías Renovables**:
  - Identificación de áreas con mayor viabilidad para proyectos solares y eólicos.

## 5. Fuentes Externas
- **Informes de Telemetría del IPSE**: Complementan el análisis energético.
- **Mapa de Poblados sin Energía**: Identificación de áreas críticas.
- **Informe Sectorial de Superservicios**: Información general sobre la energía en Colombia.

## 6. Relevancia para el Proyecto
- **Identificación de Zonas Vulnerables**: Zonas con baja cobertura energética.
- **Priorización de Hogares**: Uso de datos combinados para identificar hogares vulnerables.
- **Planificación de Energía Limpia**: Evaluación del potencial solar y eólico.
- **Predicción de la Demanda**: Herramienta para la planificación a futuro.

## 7. Enlace del Notebook
[Acceder al Notebook en Colab](https://colab.research.google.com/#fileId=https%3A//storage.googleapis.com/kaggle-colab-exported-notebooks/zni-energy-36c99958-dead-40b8-8804-d8df5bcf18c3.ipynb)
