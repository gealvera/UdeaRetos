# World Bank - Energy Access Targeting (África)

## 1. Contexto Específico
- Proyecto desarrollado en múltiples países africanos (Nigeria, Kenya, Tanzania)
- Objetivo: Identificar comunidades sin acceso a electricidad
- Escala: Regional y nacional
- Período: 2018-2022
- Desafío principal: Grandes áreas rurales sin mapeo previo

## 2. Estructura del Pipeline de ML
```
1. Recolección de Datos
   ├── Imágenes satelitales nocturnas
   ├── Datos censales
   └── Datos de encuestas de hogares

2. Preprocesamiento
   ├── Limpieza de datos satelitales
   ├── Normalización de datos censales
   └── Integración de fuentes

3. Feature Engineering
   ├── Extracción de características satelitales
   ├── Cálculo de indicadores socioeconómicos
   └── Generación de variables compuestas

4. Modelado
   ├── Entrenamiento inicial (Random Forest)
   ├── Validación geográfica
   └── Ajuste de hiperparámetros

5. Validación y Despliegue
   ├── Validación en campo
   ├── Sistema de actualización periódica
   └── Interfaz de visualización
```

## 3. Consideraciones Técnicas Específicas

### 3.1 Features Cruciales Consideradas
- **Satelitales:**
  - Luminosidad nocturna
  - Densidad de construcciones
  - Distancia a infraestructura eléctrica
  
- **Socioeconómicas:**
  - Densidad poblacional
  - Índices de pobreza
  - Actividad económica local
  
- **Infraestructura:**
  - Distancia a red eléctrica
  - Accesibilidad vial
  - Presencia de servicios públicos

### 3.2 Modelo Propuesto
- **Primera Fase:** 
  - Random Forest para clasificación inicial
  - 500 árboles
  - Validación cruzada geográfica
  
- **Segunda Fase:**
  - Gradient Boosting para refinamiento
  - Optimización bayesiana de hiperparámetros
  - Sistema de scoring ponderado

## 4. Stakeholders
- Banco Mundial (financiación y supervisión)
- Gobiernos nacionales (provisión de datos y validación)
- Agencias de energía locales (implementación)
- Comunidades locales (validación y feedback)

## 5. Datos
- **Fuentes:**
  - NASA Earth Observations
  - Censos nacionales
  - Encuestas de hogares
  - Mapeo de infraestructura eléctrica

- **Volumen:**
  - 1.2 TB de imágenes satelitales
  - Datos de 2.5 millones de hogares
  - 5 años de datos históricos

## 6. Métricas de Evaluación
- **Precisión:** 85-90%
- **Recall:** 82%
- **F1-Score:** 0.86
- **Métricas específicas:**
  - Precisión en identificación de áreas sin acceso: 92%
  - Error en estimación de población sin acceso: <8%
  - Tasa de falsos positivos en áreas rurales: <5%
