from typing import Optional
from app.pokemon import PokemonClassification
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from PIL import Image
from io import BytesIO
import numpy as np
import cv2 #lib for read image
import os

app = FastAPI()
pokemon_model = PokemonClassification("./app/pokemon1.h5")

@app.post("/predict-pokemon")
async def create_file(file: bytes = File(...)):
    stream = BytesIO(file)
    image = Image.open(stream)
    image = image.convert('RGB')
    image.save('input_img.jpg')
    sr_image = cv2.imread('input_img.jpg', cv2.IMREAD_COLOR)
    stream.close()
    val_predict = pokemon_model.predict(sr_image)
    os.remove('input_img.jpg')

    return {"Predict": val_predict}