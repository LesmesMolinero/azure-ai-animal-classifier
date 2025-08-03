# Clasificador de Imágenes con Azure Custom Vision

Este proyecto es un **clasificador de imágenes** desarrollado con [Azure Custom Vision](https://customvision.ai) que distingue entre tres categorías: **perros**, **gatos** y **conejos**.

## ¿Qué hace?
Envías una imagen (por archivo o URL), y el modelo predice a qué categoría pertenece con un porcentaje de confianza.

## Estructura del proyecto

- `predict_file.py`: predice usando una imagen local
- `predict_url.py`: predice usando una URL
- `.env`: contiene tu clave de predicción (no se sube a GitHub)
- `requirements.txt`: dependencias necesarias

## Tecnologías usadas

- Python 3.x
- Azure Custom Vision (Classification)
- `requests`
- `python-dotenv`

## Cómo ejecutar

1. Crea un archivo `.env` con tu clave de predicción:

```env
AZURE_PREDICTION_KEY="tu_clave_secreta"
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta el clasificador con:
```bash
python predict_file.py
#o
python predict_url.py
```

