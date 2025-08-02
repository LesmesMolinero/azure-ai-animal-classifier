import requests
import os
from dotenv import load_dotenv

# ✏️ Sustituye por tu URL completa para archivos
url = "https://clasificadorperrogatoconejo-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/e6f38513-6334-462a-a6da-7022a5f1acfa/classify/iterations/ClasificadorPerroGatoConejo/image"

# ✏️ Sustituye con tu clave de predicción
load_dotenv()
prediction_key = os.getenv("AZURE_PREDICTION_KEY")
image_path = "rabbits-9307357_1280.jpg"

with open(image_path, "rb") as image_file:
    headers = {
        "Prediction-Key": prediction_key,
        "Content-Type": "application/octet-stream"
    }
    response = requests.post(url, headers=headers, data=image_file)

print(response.json())
