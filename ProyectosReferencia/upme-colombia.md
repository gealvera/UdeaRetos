# UPME Colombia - Índice de Cobertura Energética

## 1. Contexto Específico
- Proyecto: "Modelo Predictivo para el Índice de Cobertura de Energía Eléctrica (ICEE)"
- Paper de referencia: "Machine Learning aplicado a la Predicción de Cobertura Energética en Colombia" (2023)
- Link al proyecto: [UPME - ICEE](https://www1.upme.gov.co/icee-ml)
- Equipo: UPME + Universidad Nacional de Colombia

## 2. Estructura del Pipeline de ML Detallada
```
1. Data Engineering Pipeline
   ├── Datos Censales
   │   ├── Procesamiento DANE
   │   ├── Datos municipales
   │   └── Estadísticas departamentales
   │
   ├── Datos de Infraestructura
   │   ├── Red eléctrica nacional
   │   ├── Subestaciones
   │   └── Capacidad instalada
   │
   └── Datos Socioeconómicos
       ├── Índices de NBI
       ├── Datos presupuestales
       └── Indicadores de desarrollo

2. Feature Engineering Pipeline
   ├── Features Geográficas
   │   ├── Índices de ruralidad
   │   ├── Dispersión poblacional
   │   └── Accesibilidad territorial
   │
   ├── Features Económicas
   │   ├── Capacidad fiscal
   │   ├── Inversión en infraestructura
   │   └── Desarrollo municipal
   │
   └── Features Técnicas
       ├── Indicadores de red
       ├── Pérdidas técnicas
       └── Eficiencia operativa

3. Model Pipeline
   ├── Regresión Logística
   │   ├── Modelado inicial
   │   └── Validación cruzada
   │
   ├── Árboles de Decisión
   │   ├── Random Forest
   │   └── Gradient Boosting
   │
   └── Ensemble
       ├── Model stacking
       ├── Validación territorial
       └── Calibración por región
```

## 3. Consideraciones Técnicas Específicas

### 3.1 Features Cruciales & Engineering
- **Análisis de Cobertura**
  ```python
  # Procesamiento de indicadores de cobertura
  def coverage_analysis(infrastructure_data):
      metrics = {
          'network_density': calculate_network_density(infrastructure_data),
          'service_quality': assess_service_quality(infrastructure_data),
          'infrastructure_age': analyze_infrastructure_age(infrastructure_data),
          'capacity_index': calculate_capacity_index(infrastructure_data)
      }
      return metrics
  ```

- **Indicadores Socioeconómicos**
  ```python
  # Cálculo de índices socioeconómicos
  def socioeconomic_indices(municipal_data):
      indices = {
          'fiscal_capacity': calculate_fiscal_strength(municipal_data),
          'development_index': compute_development_index(municipal_data),
          'poverty_metrics': analyze_poverty_levels(municipal_data),
          'investment_capacity': assess_investment_potential(municipal_data)
      }
      return indices
  ```

### 3.2 Modelo Analítico Detallado
```python
# Pseudocódigo del sistema de predicción
class CoveragePredictor:
    def __init__(self):
        self.logistic_model = LogisticRegression(
            C=1.0,
            class_weight='balanced',
            solver='lbfgs',
            max_iter=1000
        )
        self.rf_model = RandomForestClassifier(
            n_estimators=200,
            max_depth=10,
            min_samples_split=15,
            class_weight='balanced'
        )
        self.gb_model = GradientBoostingClassifier(
            n_estimators=150,
            learning_rate=0.1,
            max_depth=6
        )
        
    def train(self, X, y):
        # Fase 1: Regresión Logística
        log_pred = self.logistic_model.fit_predict_proba(X, y)
        
        # Fase 2: Random Forest
        rf_pred = self.rf_model.fit_predict_proba(X, y)
        
        # Fase 3: Gradient Boosting
        gb_pred = self.gb_model.fit_predict_proba(X, y)
        
        # Ensemble con ponderación regional
        final_pred = self.regional_weighted_ensemble(
            log_pred,
            rf_pred,
            gb_pred,
            X['region']
        )
        return final_pred
```

## 4. Datasets Detallados
1. **Dataset de Infraestructura**
   - Fuente: SIN + UPME
   - Cobertura: Nacional
   - Variables:
     ```json
     {
       "red_electrica": [
         "longitud_redes",
         "capacidad_transformacion",
         "estado_infraestructura"
       ],
       "operacion": [
         "perdidas_tecnicas",
         "calidad_servicio",
         "interrupciones"
       ],
       "cobertura": [
         "usuarios_conectados",
         "demanda_potencial",
         "crecimiento_red"
       ]
     }
     ```

2. **Dataset Municipal**
   - Fuente: DANE + DNP
   - Registros: 1,103 municipios
   - Variables:
     ```json
     {
       "demografico": [
         "poblacion_total",
         "distribucion_rural_urbana",
         "densidad_poblacional"
       ],
       "economico": [
         "presupuesto_municipal",
         "inversion_infraestructura",
         "recaudo_fiscal"
       ],
       "desarrollo": [
         "nbi",
         "ipv",
         "cobertura_servicios"
       ]
     }
     ```

3. **Dataset Operativo**
   - Fuente: Operadores de Red
   - Período: 2020-2023
   - Métricas:
     ```json
     {
       "tecnicas": [
         "consumo_promedio",
         "factor_carga",
         "eficiencia_distribucion"
       ],
       "comerciales": [
         "facturacion",
         "morosidad",
         "nuevas_conexiones"
       ],
       "calidad": [
         "saidi",
         "saifi",
         "reclamos"
       ]
     }
     ```

## 5. Resultados Analíticos
- **Métricas de Performance**
  ```python
  {
      'accuracy': 0.79,
      'precision': 0.81,
      'recall': 0.77,
      'f1_score': 0.79,
      'auc_roc': 0.83,
      'kappa': 0.75
  }
  ```

- **Feature Importance Top 10**
  ```python
  {
      'densidad_poblacional': 0.16,
      'capacidad_fiscal': 0.14,
      'infraestructura_existente': 0.13,
      'nbi': 0.11,
      'inversion_historica': 0.10,
      'distancia_red': 0.09,
      'perdidas_tecnicas': 0.08,
      'demanda_potencial': 0.07,
      'crecimiento_poblacional': 0.06,
      'eficiencia_operativa': 0.06
  }
  ```

## 6. Enlaces y Referencias
- [GitHub Repository](https://github.com/upme-colombia/icee-ml)
- [Documentación Técnica](https://www1.upme.gov.co/Documents/icee-ml-docs)
- [Portal de Datos](https://datos.upme.gov.co/icee)
- Paper: "Modelamiento Predictivo del ICEE en Colombia: Un Enfoque de Machine Learning" (2023)

