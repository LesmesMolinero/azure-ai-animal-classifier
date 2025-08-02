import requests
import os
from dotenv import load_dotenv

# URL del endpoint para imágenes por URL (fíjate en `/url`)
url = "https://clasificadorperrogatoconejo-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/e6f38513-6334-462a-a6da-7022a5f1acfa/classify/iterations/ClasificadorPerroGatoConejo/url"

# Clave de predicción (igual que en el anterior)
load_dotenv()
prediction_key = os.getenv("AZURE_PREDICTION_KEY")
# URL de una imagen pública (debes usar una imagen online accesible)
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/VAN_CAT.png/800px-VAN_CAT.png"

headers = {
    "Prediction-Key": prediction_key,
    "Content-Type": "application/json"
}

body = {
    "Url": image_url
}

response = requests.post(url, headers=headers, json=body)

print(response.json())
