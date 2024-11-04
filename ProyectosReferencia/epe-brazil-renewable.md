# EPE Brasil - Priorización de Energías Renovables en Comunidades Vulnerables

## 1. Contexto Específico
- Proyecto: "ML para Universalização de Energia Renovável em Comunidades Vulneráveis"
- Paper de referencia: "Machine Learning na Priorização de Comunidades para Energia Renovável" (2023)
- Link al proyecto: [EPE - Energias Renováveis](https://www.epe.gov.br/pt/projetos/ml-energias-renovaveis)
- Equipo: EPE + Universidad Federal de Rio de Janeiro

## 2. Estructura del Pipeline de ML Detallada
```
1. Data Engineering Pipeline
   ├── Datos Ambientales
   │   ├── Radiación solar
   │   ├── Recursos hídricos
   │   └── Condiciones climáticas
   │
   ├── Datos Socioeconómicos
   │   ├── Censo IBGE
   │   ├── Índices de desarrollo
   │   └── Indicadores de pobreza
   │
   └── Datos de Infraestructura
       ├── Red eléctrica existente
       ├── Accesibilidad
       └── Recursos locales

2. Feature Engineering Pipeline
   ├── Features Ambientales
   │   ├── Potencial renovable
   │   ├── Riesgos naturales
   │   └── Sostenibilidad
   │
   ├── Features Sociales
   │   ├── Vulnerabilidad
   │   ├── Capacidad comunitaria
   │   └── Demanda energética
   │
   └── Features Técnicas
       ├── Viabilidad técnica
       ├── Costos estimados
       └── Mantenimiento

3. Model Pipeline
   ├── LightGBM
   │   ├── Clasificación inicial
   │   └── Feature selection
   │
   ├── CatBoost
   │   ├── Refinamiento
   │   └── Categorical handling
   │
   └── Ensemble
       ├── Weighted averaging
       ├── Regional validation
       └── Temporal testing
```

## 3. Consideraciones Técnicas Específicas

### 3.1 Features Cruciales & Engineering
- **Análisis de Potencial Renovable**
  ```python
  # Evaluación de recursos renovables
  def renewable_potential_analysis(environmental_data):
      potential = {
          'solar_resource': calculate_solar_potential(environmental_data),
          'hydro_potential': assess_hydro_resources(environmental_data),
          'biomass_availability': evaluate_biomass(environmental_data),
          'seasonal_variations': analyze_seasonality(environmental_data)
      }
      return potential
  ```

- **Evaluación Comunitaria**
  ```python
  # Análisis de capacidad comunitaria
  def community_assessment(social_data):
      metrics = {
          'organizational_capacity': evaluate_organization(social_data),
          'economic_potential': assess_economic_capacity(social_data),
          'technical_skills': evaluate_local_skills(social_data),
          'community_engagement': measure_engagement(social_data)
      }
      return metrics
  ```

### 3.2 Modelo Analítico Detallado
```python
# Pseudocódigo del sistema de clasificación
class RenewableEnergyPrioritizer:
    def __init__(self):
        self.lgb_model = LGBMClassifier(
            n_estimators=500,
            learning_rate=0.05,
            num_leaves=31,
            feature_fraction=0.8
        )
        
        self.cat_model = CatBoostClassifier(
            iterations=1000,
            learning_rate=0.03,
            depth=6,
            loss_function='Logloss'
        )
        
    def train(self, X, y):
        # Fase 1: LightGBM
        lgb_pred = self.lgb_model.fit_predict_proba(X, y)
        
        # Análisis de características
        feature_importance = self.lgb_model.feature_importances_
        
        # Fase 2: CatBoost con features seleccionadas
        selected_features = self.select_top_features(feature_importance)
        cat_pred = self.cat_model.fit_predict_proba(
            X[selected_features], 
            y
        )
        
        # Ensemble con pesos regionales
        final_pred = self.regional_weighted_ensemble(
            lgb_pred,
            cat_pred,
            X['region']
        )
        return final_pred
```

## 4. Datasets Detallados
1. **Dataset Ambiental**
   - Fuente: INPE + INMET
   - Cobertura: Nacional
   - Variables:
     ```json
     {
       "solar": [
         "radiacion_directa",
         "radiacion_difusa",
         "horas_sol"
       ],
       "hidrico": [
         "precipitacion",
         "caudales",
         "recursos_subterraneos"
       ],
       "climatico": [
         "temperatura",
         "humedad",
         "vientos"
       ]
     }
     ```

2. **Dataset Socioeconómico**
   - Fuente: IBGE + IPEA
   - Registros: 2.5M hogares
   - Variables:
     ```json
     {
       "demografico": [
         "composicion_familiar",
         "educacion",
         "ocupacion"
       ],
       "economico": [
         "renta_familiar",
         "actividades_productivas",
         "gastos_energia"
       ],
       "social": [
         "organizacion_comunitaria",
         "participacion_social",
         "vulnerabilidad"
       ]
     }
     ```

3. **Dataset Técnico**
   - Fuente: EPE + ANEEL
   - Cobertura: Comunidades objetivo
   - Métricas:
     ```json
     {
       "infraestructura": [
         "acceso_actual",
         "estado_instalaciones",
         "potencial_expansion"
       ],
       "tecnico": [
         "capacidad_instalacion",
         "mantenimiento_requerido",
         "vida_util"
       ],
       "operacional": [
         "costos_operacion",
         "eficiencia_esperada",
         "perdidas_estimadas"
       ]
     }
     ```

## 5. Resultados Analíticos
- **Métricas de Performance**
  ```python
  {
      'accuracy': 0.86,
      'precision': 0.88,
      'recall': 0.85,
      'f1_score': 0.86,
      'auc_roc': 0.89,
      'kappa': 0.83
  }
  ```

- **Feature Importance Top 10**
  ```python
  {
      'potencial_solar': 0.16,
      'vulnerabilidad_social': 0.14,
      'accesibilidad': 0.12,
      'capacidad_organizativa': 0.11,
      'costo_implementacion': 0.10,
      'demanda_energia': 0.09,
      'recursos_locales': 0.08,
      'participacion_comunitaria': 0.07,
      'viabilidad_tecnica': 0.07,
      'sostenibilidad': 0.06
  }
  ```

## 6. Enlaces y Referencias
- [GitHub Repository](https://github.com/epe-brasil/renewable-energy-ml)
- [Documentación Técnica](https://www.epe.gov.br/docs/ml-renovaveis)
- [Portal de Datos](https://dados.epe.gov.br/renovaveis)
- Paper: "Machine Learning Applications in Renewable Energy Planning for Vulnerable Communities in Brazil" (2023)

