# Chile - Caracterización de Pobreza Energética

## 1. Contexto Específico
- Proyecto: "Identificación y Caracterización de Pobreza Energética mediante ML"
- Paper de referencia: "Machine Learning para la Caracterización de Pobreza Energética en Chile" (2022)
- Link al proyecto: [Ministerio de Energía - Pobreza Energética](https://energia.gob.cl/proyectos/caracterizacion-pobreza-energetica)
- Equipo: División de Acceso y Equidad Energética + Universidad de Chile

## 2. Estructura del Pipeline de ML Detallada
```
1. Data Engineering Pipeline
   ├── Procesamiento de Encuestas
   │   ├── Casen (Caracterización Socioeconómica)
   │   ├── EPF (Encuesta Presupuestos Familiares)
   │   └── Encuesta de Pobreza Energética
   │
   ├── Datos Territoriales
   │   ├── División administrativa
   │   ├── Indicadores climáticos
   │   └── Acceso a servicios
   │
   └── Datos Energéticos
       ├── Consumo por tipo de energético
       ├── Calidad de servicio
       └── Precios de energía

2. Feature Engineering Pipeline
   ├── Clustering Inicial
   │   ├── K-means para zonificación
   │   ├── DBSCAN para detección de clusters
   │   └── Validación de clusters
   │
   ├── Features Compuestas
   │   ├── Índices de vulnerabilidad
   │   ├── Indicadores de acceso
   │   └── Métricas de calidad
   │
   └── Features Territoriales
       ├── Índices de ruralidad
       ├── Accesibilidad
       └── Zonificación climática

3. Model Pipeline
   ├── Clustering
   │   ├── K-means++
   │   └── Análisis de silhouette
   │
   ├── Clasificación
   │   ├── XGBoost
   │   └── Random Forest
   │
   └── Ensemble
       ├── Stacking
       ├── Validación cruzada territorial
       └── Calibración por zona
```

## 3. Consideraciones Técnicas Específicas

### 3.1 Features Cruciales & Engineering
- **Clustering Territorial**
  ```python
  # Ejemplo de procesamiento de clusters territoriales
  def territorial_clustering(geographic_data):
      clusters = {
          'urban_rural': calculate_urban_rural_index(geographic_data),
          'climate_zone': assign_climate_zone(geographic_data),
          'accessibility': calculate_accessibility_score(geographic_data),
          'service_coverage': service_coverage_index(geographic_data)
      }
      return clusters
  ```

- **Índices de Vulnerabilidad**
  ```python
  # Cálculo del índice de vulnerabilidad energética
  def vulnerability_index(household_data, territorial_data):
      components = {
          'income_energy_ratio': 0.30,
          'energy_quality': 0.25,
          'territorial_factors': 0.25,
          'housing_conditions': 0.20
      }
      return weighted_vulnerability_score(household_data, 
                                       territorial_data, 
                                       components)
  ```

### 3.2 Modelo Analítico Detallado
```python
# Pseudocódigo del sistema híbrido clustering-clasificación
class EnergyPovertyAnalyzer:
    def __init__(self):
        self.clusterer = KMeans(
            n_clusters=5,
            init='k-means++',
            n_init=10
        )
        self.xgb_model = XGBClassifier(
            max_depth=6,
            learning_rate=0.1,
            n_estimators=250,
            objective='multi:softprob'
        )
        self.rf_model = RandomForestClassifier(
            n_estimators=200,
            max_depth=8,
            min_samples_split=15
        )
        
    def analyze(self, X, y):
        # Fase 1: Clustering territorial
        clusters = self.clusterer.fit_predict(X)
        
        # Fase 2: Feature engineering por cluster
        enhanced_features = self.generate_cluster_features(X, clusters)
        
        # Fase 3: Clasificación por zona
        xgb_pred = self.xgb_model.fit_predict(enhanced_features, y)
        rf_pred = self.rf_model.fit_predict(enhanced_features, y)
        
        # Ensemble final con pesos por zona
        final_pred = self.zone_weighted_ensemble(xgb_pred, rf_pred, clusters)
        return final_pred, clusters
```

## 4. Datasets Detallados
1. **Dataset Socioeconómico**
   - Fuente: CASEN 2022
   - Registros: 950K hogares
   - Variables:
     ```json
     {
       "demograficos": [
         "composicion_hogar",
         "nivel_educacional",
         "situacion_laboral"
       ],
       "economicos": [
         "ingreso_total",
         "gasto_energia",
         "subsidios"
       ],
       "vivienda": [
         "tipo_vivienda",
         "material_construccion",
         "aislacion_termica"
       ]
     }
     ```

2. **Dataset Energético**
   - Fuente: Superintendencia de Electricidad y Combustibles
   - Cobertura: Nacional
   - Métricas:
     ```json
     {
       "consumo": [
         "electricidad_kwh",
         "gas_m3",
         "lena_kg"
       ],
       "calidad": [
         "interrupciones_suministro",
         "variaciones_tension",
         "tiempo_reposicion"
       ],
       "costos": [
         "tarifa_electrica",
         "precio_combustibles",
         "gasto_calefaccion"
       ]
     }
     ```

3. **Dataset Territorial**
   - Fuente: IDE Chile
   - Cobertura: Nacional
   - Variables:
     ```json
     {
       "geograficas": [
         "coordenadas",
         "altura",
         "pendiente"
       ],
       "climaticas": [
         "zona_termica",
         "precipitacion",
         "temperatura"
       ],
       "accesibilidad": [
         "distancia_centros_urbanos",
         "conectividad_vial",
         "servicios_basicos"
       ]
     }
     ```

## 5. Resultados Analíticos
- **Métricas de Performance**
  ```python
  {
      'accuracy_global': 0.85,
      'precision_por_zona': {
          'zona_norte': 0.83,
          'zona_centro': 0.86,
          'zona_sur': 0.84
      },
      'recall_promedio': 0.82,
      'f1_score': 0.83,
      'silhouette_score': 0.71
  }
  ```

- **Importancia de Features Top 10**
  ```python
  {
      'ingreso_energia_ratio': 0.16,
      'calidad_vivienda': 0.14,
      'zona_climatica': 0.12,
      'acceso_servicios': 0.11,
      'tipo_calefaccion': 0.10,
      'nivel_educacional': 0.09,
      'hacinamiento': 0.08,
      'distancia_servicios': 0.07,
      'edad_vivienda': 0.07,
      'composicion_familiar': 0.06
  }
  ```

## 6. Enlaces y Referencias
- [GitHub Repository](https://github.com/minenergia-chile/energy-poverty-ml)
- [Documentación Técnica](https://energia.gob.cl/documentacion/pobreza-energetica)
- [Acceso a Datos](https://datos.gob.cl/dataset/pobreza-energetica)
- Paper: "Clasificación Híbrida para la Caracterización de Pobreza Energética en Chile" (2023)

