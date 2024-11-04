# World Bank - Energy Access Targeting (África)

## 1. Contexto Específico
- Proyecto: "Machine Learning for Energy Access Planning"
- Paper de referencia: "Using Machine Learning and Remote Sensing to Value Energy Infrastructure Site Selection" (2020)
- Link al proyecto: [World Bank Energy Access Project](https://www.worldbank.org/en/topic/energy/publication/machine-learning-for-energy-access)
- Equipo: Data Science Team del World Bank's Energy Sector Management Assistance Program (ESMAP)

## 2. Estructura del Pipeline de ML Detallada
```
1. Data Engineering Pipeline
   ├── Satellite Data Processing
   │   ├── Nighttime lights preprocessing
   │   ├── Daytime imagery feature extraction
   │   └── Temporal aggregation (monthly composites)
   │
   ├── Survey Data Integration
   │   ├── Household survey cleaning
   │   ├── Geospatial matching
   │   └── Feature aggregation
   │
   └── External Data Sources
       ├── OpenStreetMap features
       ├── Population density
       └── Economic indicators

2. Feature Engineering Pipeline
   ├── Spatial Features
   │   ├── Distance to infrastructure
   │   ├── Population density gradients
   │   └── Urban/rural classification
   │
   ├── Temporal Features
   │   ├── Seasonal patterns
   │   ├── Growth indicators
   │   └── Change detection
   │
   └── Socioeconomic Features
       ├── Wealth index calculation
       ├── Economic activity proxies
       └── Infrastructure access scores

3. Model Pipeline
   ├── Initial Classification
   │   ├── Random Forest (RF)
   │   └── Feature importance analysis
   │
   ├── Refinement
   │   ├── XGBoost
   │   └── Hyperparameter optimization
   │
   └── Ensemble Integration
       ├── Model stacking
       ├── Weighted averaging
       └── Calibration
```

## 3. Consideraciones Técnicas Específicas

### 3.1 Features Cruciales & Engineering
- **Satelitales (Resolución: 30m)**
  ```python
  # Ejemplo de feature engineering para datos satelitales
  def calculate_nightlight_features(image_data):
      features = {
          'mean_luminosity': np.mean(image_data),
          'std_luminosity': np.std(image_data),
          'max_luminosity': np.max(image_data),
          'luminosity_gradient': calculate_gradient(image_data)
      }
      return features
  ```

- **Socioeconómicas**
  ```python
  # Ejemplo de cálculo de índice de vulnerabilidad
  def vulnerability_index(household_data):
      weights = {
          'income': 0.4,
          'education': 0.3,
          'infrastructure': 0.3
      }
      return weighted_score(household_data, weights)
  ```

### 3.2 Modelo Analítico Detallado
```python
# Pseudocódigo del pipeline principal
class EnergyAccessModel:
    def __init__(self):
        self.rf_model = RandomForestClassifier(
            n_estimators=500,
            max_depth=10,
            min_samples_split=20
        )
        self.xgb_model = XGBClassifier(
            learning_rate=0.1,
            max_depth=7,
            n_estimators=200
        )
        
    def train(self, X, y):
        # Primera fase: Random Forest
        rf_pred = self.rf_model.fit_predict(X, y)
        
        # Feature importance analysis
        importances = self.rf_model.feature_importances_
        
        # Segunda fase: XGBoost con features importantes
        important_features = select_top_features(importances)
        xgb_pred = self.xgb_model.fit_predict(X[important_features], y)
        
        # Ensemble mediante stacking
        final_pred = self.ensemble_predictions(rf_pred, xgb_pred)
        return final_pred
```

## 4. Datasets Detallados
1. **Satellite Imagery Dataset**
   - Fuente: NASA VIIRS
   - Período: 2018-2022
   - Resolución: 30m
   - Variables:
     ```json
     {
       "bands": ["visible", "infrared", "nightlights"],
       "temporal_resolution": "monthly",
       "spatial_coverage": "country-wide",
       "size": "800GB compressed"
     }
     ```

2. **Household Survey Data**
   - Fuente: Living Standards Measurement Study (LSMS)
   - Registros: 2.5M hogares
   - Variables clave:
     ```json
     {
       "demographic": ["household_size", "education_level", "income"],
       "energy": ["current_access", "consumption", "willingness_to_pay"],
       "geographic": ["lat", "long", "admin_region"]
     }
     ```

3. **Infrastructure Data**
   - Fuente: OpenStreetMap + Government Records
   - Cobertura: Nacional
   - Elementos:
     ```json
     {
       "grid": ["transmission_lines", "transformers", "substations"],
       "transport": ["roads", "railways"],
       "facilities": ["schools", "hospitals", "markets"]
     }
     ```

## 5. Resultados Analíticos
- **Model Performance Metrics**
  ```python
  {
      'accuracy': 0.89,
      'precision': 0.87,
      'recall': 0.85,
      'f1_score': 0.86,
      'auc_roc': 0.91
  }
  ```

- **Feature Importance Top 10**
  ```python
  {
      'night_lights_mean': 0.15,
      'distance_to_grid': 0.14,
      'population_density': 0.12,
      'household_income': 0.11,
      'infrastructure_index': 0.10,
      'education_level': 0.09,
      'road_access': 0.08,
      'economic_activity': 0.07,
      'seasonal_variation': 0.07,
      'urbanization_level': 0.07
  }
  ```

## 6. Enlaces y Referencias
- [GitHub Repository](https://github.com/worldbank/energy-access-ml)
- [Technical Documentation](https://documents.worldbank.org/en/publication/energy-access-ml-technical)
- [Dataset Access](https://datacatalog.worldbank.org/energy-access)
- Paper: "Machine Learning for Energy Access: Lessons from the Field" (2021)

