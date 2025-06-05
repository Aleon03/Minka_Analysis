<center>
<img src="images/embimos-positivo.png" width="400">

<center>
<img src="images/minka-logo.png"  width="400">



# Proyecto Minka - Generador de Informes Mensuales

Este proyecto automatiza la generación de informes mensuales para el proyecto de ciencia ciudadana Minka ([https://minka-sdg.org](https://minka-sdg.org)), extrayendo datos de observaciones de biodiversidad, procesándolos y generando un documento Word con métricas, gráficos y análisis de cualquier proyecto que se pueda encontrar en la plataforma.

## Funcionamiento

El script principal (`minka_docx_execution.py`) realiza las siguientes operaciones:

### Obtención i Generación de los datos:

- Descarga observaciones de los proyectos desde la API de Minka
- Procesa los datos en DataFrames de observaciones y fotos

### Cálculo de métricas:

- Métricas principales (observaciones, observadores, identificadores, especies)
- Evolución mensual de estas métricas
- Conteo de taxones por diferentes niveles (reino, filo, clase, etc.)
- Detección de nuevas especies registradas

### Generación de gráficos:

- Gráficos de evolución mensual
- Gráficos de taxones más observados
- Mapas de calor de distribución geográfica
- Fotos de nuevas especies con metadatos

### Creación del informe DOCX:
- Documento estructurado con todas las métricas y gráficos
- Hipervínculos a observaciones originales

## Organización del código

El proyecto está organizado en dos archivos principales:

### `minka_docx_execution.py`:
- Script principal que orquesta todo el proceso
- Secuencia lógica de obtención, procesamiento y generación
- Verificación de archivos generados

### `utils.py`:
- Funciones auxiliares agrupadas por propósito:
  - Gestión de directorios
  - Obtención de datos de la API
  - Procesamiento y cálculo de métricas
  - Generación de gráficos y visualizaciones
  - Construcción del documento Word

La estructura de directorios creada incluye:
- `data/`: Se alojan los archivos .csv necesarios para obtener todos los datos
- `figures/`: Gráficos de todos los apartados
- `minka_photos/`: Fotografías descargadas de las nuevas especies
- `minka_photos_new_species/`: Fotos con los metadatos de las nuevas especies registradas


## Producto final

El resultado es un documento Word (`informe_mensual_minka.docx`) que contiene:
- Resumen ejecutivo con métricas clave
- Gráficos temporales de actividad
- Análisis taxonómico por diferentes niveles
- Mapas de distribución geográfica
- Listado y fotos de nuevas especies registradas
- Enlaces a las observaciones originales

