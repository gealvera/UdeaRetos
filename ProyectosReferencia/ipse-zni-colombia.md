# IPSE Colombia - Priorización ZNI

## 1. Contexto Específico
- Proyecto: "Sistema ML para Priorización de Inversiones en Zonas No Interconectadas"
- Paper de referencia: "Deep Learning para la Clasificación y Priorización de ZNI en Colombia" (2023)
- Link al proyecto: [IPSE - ZNI ML](https://www.ipse.gov.co/proyectos/ml-zni)
- Equipo: IPSE + Universidad de Los Andes

## 2. Estructura del Pipeline de ML Detallada
```
1. Data Engineering Pipeline
   ├── Datos Geoespaciales
   │   ├── Imágenes satelitales
   │   ├── Mapeo territorial
   │   └── Análisis topográfico
   │
   ├── Datos Sociales ZNI
   │   ├── Censos comunitarios
   │   ├── Encuestas locales
   │   └── Caracterización social
   │
   └── Datos de Proyectos
       ├── Histórico de intervenciones
       ├── Costos de implementación
       └── Resultados previos

2. Feature Engineering Pipeline
   ├── Features Satelitales
   │   ├── Procesamiento de imágenes
   │   ├── Extracción de patrones
   │   └── Índices de desarrollo
   │
   ├── Features Sociales
   │   ├── Índices de necesidad
   │   ├── Potencial de impacto
   │   └── Sostenibilidad
   │
   └── Features Técnicas
       ├── Viabilidad técnica
       ├── Costos estimados
       └── Factibilidad operativa

3. Model Pipeline
   ├── CNN para Imágenes
   │   ├── Procesamiento visual
   │   └── Feature extraction
   │
   ├── Deep Neural Network
   │   ├── Dense layers
   │   └── Dropout regularization
   │
   └── Ensemble
       ├── Model integration
       ├── Spatial validation
       └── Temporal testing
```

## 3. Consideraciones Técnicas Específicas

### 3.1 Features Cruciales & Engineering
- **Procesamiento de Imágenes Satelitales**
  ```python
  # Procesamiento de datos satelitales
  def satellite_processing(image_data):
      features = {
          'settlement_density': detect_settlements(image_data),
          'vegetation_index': calculate_ndvi(image_data),
          'water_bodies': detect_water(image_data),
          'infrastructure': detect_infrastructure(image_data)
      }
      return features
  ```

- **Análisis de Viabilidad**
  ```python
  # Cálculo de índices de viabilidad
  def viability_analysis(zone_data):
      indices = {
          'technical_feasibility': assess_technical_aspects(zone_data),
          'social_sustainability': evaluate_social_factors(zone_data),
          'economic_viability': calculate_economic_metrics(zone_data),
          'environmental_impact': assess_environmental_factors(zone_data)
      }
      return indices
  ```

### 3.2 Modelo Analítico Detallado
```python
# Pseudocódigo del sistema de clasificación neuronal
class ZNIPrioritizer:
    def __init__(self):
        self.cnn_model = Sequential([
            Conv2D(32, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Flatten(),
            Dense(64, activation='relu')
        ])
        
        self.dnn_model = Sequential([
            Dense(128, activation='relu'),
            Dropout(0.3),
            Dense(64, activation='relu'),
            Dropout(0.2),
            Dense(32, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        
    def train(self, X_img, X_tab, y):
        # Fase 1: Procesamiento CNN
        img_features = self.cnn_model.fit(X_img)
        
        # Fase 2: Integración con datos tabulares
        combined_features = self.combine_features(
            img_features,
            X_tab
        )
        
        # Fase 3: Clasificación final
        final_pred = self.dnn_model.fit(combined_features, y)
        
        return final_pred
```

## 4. Datasets Detallados
1. **Dataset Satelital**
   - Fuente: Sentinel-2 + Planet Labs
   - Resolución: 10m
   - Variables:
     ```json
     {
       "bandas_espectrales": [
         "rgb",
         "infrarrojo",
         "ndvi"
       ],
       "cobertura": [
         "uso_suelo",
         "densidad_edificaciones",
         "accesibilidad"
       ],
       "temporal": [
         "cambios_estacionales",
         "desarrollo_historico",
         "patrones_crecimiento"
       ]
     }
     ```

2. **Dataset Social ZNI**
   - Fuente: IPSE + Comunidades
   - Registros: 1,710 comunidades
   - Variables:
     ```json
     {
       "demografico": [
         "poblacion_total",
         "estructura_etaria",
         "grupos_etnicos"
       ],
       "economico": [
         "actividades_productivas",
         "ingresos_promedio",
         "capacidad_pago"
       ],
       "energia": [
         "consumo_actual",
         "fuentes_energia",
         "necesidades_energeticas"
       ]
     }
     ```

3. **Dataset Técnico**
   - Fuente: IPSE + Consultores
   - Cobertura: Nacional ZNI
   - Métricas:
     ```json
     {
       "tecnico": [
         "recurso_renovable",
         "condiciones_terreno",
         "infraestructura_existente"
       ],
       "operativo": [
         "costos_estimados",
         "mantenimiento_requerido",
         "logistica_implementacion"
       ],
       "sostenibilidad": [
         "capacidad_local",
         "soporte_tecnico",
         "durabilidad_esperada"
       ]
     }
     ```

## 5. Resultados Analíticos
- **Métricas de Performance**
  ```python
  {
      'accuracy': 0.84,
      'precision': 0.86,
      'recall': 0.83,
      'f1_score': 0.84,
      'auc_roc': 0.87,
      'kappa': 0.81
  }
  ```

- **Feature Importance Top 10**
  ```python
  {
      'poblacion_beneficiada': 0.15,
      'viabilidad_tecnica': 0.14,
      'costo_beneficio': 0.13,
      'accesibilidad': 0.11,
      'recurso_renovable': 0.10,
      'capacidad_comunitaria': 0.09,
      'impacto_social': 0.08,
      'sostenibilidad': 0.08,
      'infraestructura_actual': 0.07,
      'potencial_productivo': 0.05
  }
  ```

## 6. Enlaces y Referencias
- [GitHub Repository](https://github.com/ipse-colombia/zni-ml)
- [Documentación Técnica](https://www.ipse.gov.co/docs/zni-ml-documentation)
- [Portal de Datos](https://datos.ipse.gov.co/zni)
- Paper: "Deep Learning Applications in Rural Electrification Planning: A Colombian Case Study" (2023)

