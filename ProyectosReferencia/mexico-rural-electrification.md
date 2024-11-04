# México - Programa de Electrificación Rural

## 1. Contexto Específico
- Proyecto: "ML para Priorización de Electrificación Rural en México"
- Paper de referencia: "Machine Learning y SIG en la Planificación de Electrificación Rural" (2023)
- Link al proyecto: [SENER - Electrificación Rural](https://www.gob.mx/sener/electrificacion-rural)
- Equipo: SENER + INEEL (Instituto Nacional de Electricidad y Energías Limpias)

## 2. Estructura del Pipeline de ML Detallada
```
1. Data Engineering Pipeline
   ├── Datos Geoespaciales
   │   ├── Procesamiento SIG
   │   ├── Datos satelitales
   │   └── Integración OpenStreetMap
   │
   ├── Datos Móviles
   │   ├── Procesamiento CDR (Call Detail Records)
   │   ├── Patrones de movilidad
   │   └── Densidad poblacional
   │
   └── Datos Socioeconómicos
       ├── CONEVAL (Pobreza)
       ├── INEGI (Censo)
       └── Encuestas específicas

2. Feature Engineering Pipeline
   ├── Features Geoespaciales
   │   ├── Distancias a infraestructura
   │   ├── Análisis de terreno
   │   └── Zonificación
   │
   ├── Features Temporales
   │   ├── Patrones de actividad
   │   ├── Estacionalidad
   │   └── Tendencias de desarrollo
   │
   └── Features Socioeconómicas
       ├── Índices de marginación
       ├── Indicadores de desarrollo
       └── Potencial económico

3. Model Pipeline
   ├── Random Forest
   │   ├── Clasificación inicial
   │   └── Feature ranking
   │
   ├── SVM
   │   ├── Clasificación refinada
   │   └── Kernel optimization
   │
   └── Ensemble
       ├── Weighted voting
       ├── Geographic validation
       └── Temporal cross-validation
```

## 3. Consideraciones Técnicas Específicas

### 3.1 Features Cruciales & Engineering
- **Análisis Geoespacial**
  ```python
  # Procesamiento de datos geoespaciales
  def spatial_feature_engineering(gis_data):
      features = {
          'distance_to_grid': calculate_grid_distance(gis_data),
          'terrain_complexity': terrain_analysis(gis_data),
          'population_density': calculate_density(gis_data),
          'accessibility_index': calculate_accessibility(gis_data)
      }
      return features
  ```

- **Procesamiento CDR**
  ```python
  # Análisis de datos móviles
  def mobile_data_analysis(cdr_data):
      patterns = {
          'activity_density': calculate_activity_patterns(cdr_data),
          'movement_flows': analyze_movements(cdr_data),
          'temporal_presence': temporal_analysis(cdr_data),
          'economic_activity': estimate_economic_activity(cdr_data)
      }
      return patterns
  ```

### 3.2 Modelo Analítico Detallado
```python
# Pseudocódigo del sistema de clasificación ensemble
class RuralElectrificationClassifier:
    def __init__(self):
        self.rf_classifier = RandomForestClassifier(
            n_estimators=300,
            max_depth=12,
            min_samples_split=10,
            class_weight='balanced'
        )
        self.svm_classifier = SVC(
            kernel='rbf',
            C=1.0,
            probability=True,
            class_weight='balanced'
        )
        
    def train(self, X, y):
        # Fase 1: Random Forest
        rf_probas = self.rf_classifier.fit_predict_proba(X, y)
        
        # Feature importance y selección
        important_features = self.select_top_features(
            self.rf_classifier.feature_importances_
        )
        
        # Fase 2: SVM con features seleccionadas
        svm_probas = self.svm_classifier.fit_predict_proba(
            X[important_features], y
        )
        
        # Ensemble con pesos geográficos
        final_pred = self.geographic_weighted_ensemble(
            rf_probas, 
            svm_probas,
            X['geographic_zone']
        )
        return final_pred
```

## 4. Datasets Detallados
1. **Dataset Geoespacial**
   - Fuente: INEGI + OpenStreetMap
   - Cobertura: Nacional
   - Variables:
     ```json
     {
       "infraestructura": [
         "red_electrica",
         "vias_acceso",
         "centros_poblacion"
       ],
       "terreno": [
         "elevacion",
         "pendiente",
         "uso_suelo"
       ],
       "demografico": [
         "densidad_poblacional",
         "dispersion_poblacional",
         "patrones_asentamiento"
       ]
     }
     ```

2. **Dataset CDR**
   - Fuente: Operadores Móviles
   - Período: 2021-2023
   - Métricas:
     ```json
     {
       "movilidad": [
         "flujos_origen_destino",
         "patrones_diarios",
         "estacionalidad"
       ],
       "actividad": [
         "densidad_llamadas",
         "uso_datos",
         "presencia_temporal"
       ],
       "economica": [
         "actividad_comercial",
         "patrones_laborales",
         "desarrollo_local"
       ]
     }
     ```

3. **Dataset Socioeconómico**
   - Fuente: CONEVAL + INEGI
   - Registros: 2.1M hogares
   - Variables:
     ```json
     {
       "pobreza": [
         "ingreso_hogar",
         "carencias_sociales",
         "indice_rezago"
       ],
       "vivienda": [
         "caracteristicas_construccion",
         "servicios_basicos",
         "hacinamiento"
       ],
       "desarrollo": [
         "educacion",
         "salud",
         "empleo"
       ]
     }
     ```

## 5. Resultados Analíticos
- **Métricas de Performance**
  ```python
  {
      'accuracy': 0.88,
      'precision': 0.86,
      'recall': 0.85,
      'f1_score': 0.85,
      'auc_roc': 0.90,
      'kappa': 0.83
  }
  ```

- **Feature Importance Top 10**
  ```python
  {
      'distancia_red': 0.18,
      'densidad_poblacional': 0.15,
      'indice_marginacion': 0.13,
      'accesibilidad': 0.11,
      'actividad_economica': 0.10,
      'densidad_telefonica': 0.09,
      'tipo_terreno': 0.08,
      'servicios_basicos': 0.07,
      'educacion': 0.05,
      'hacinamiento': 0.04
  }
  ```

## 6. Enlaces y Referencias
- [GitHub Repository](https://github.com/sener-mexico/rural-electrification-ml)
- [Documentación Técnica](https://www.gob.mx/sener/documentos/electrificacion-rural-ml)
- [Portal de Datos](https://datos.gob.mx/electrificacion-rural)
- Paper: "Integración de Machine Learning y GIS para la Planificación de Electrificación Rural en México" (2023)

