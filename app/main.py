from typing import Optional
from app.pokemon import PokemonClassification
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow as tf
import cv2 #lib for read image
import os

app = FastAPI()
pokemon_model = PokemonClassification("./app/pokemon1.h5")

@app.post("/predict-pokemon")
async def create_file(file: bytes = File(...)):
    stream = BytesIO(file)
    # image = tf.keras.preprocessing.image.img_to_array(Image.open(stream),'channels_first')
    image = Image.open(stream)
    print('--Mode Before Convert--')
    print(image.mode)
    image = image.convert('RGB')
    print('--Mode After Convert--')
    print(image.mode)
    image.save('test_convert.jpg')
    sr_image = cv2.imread('test_convert.jpg', cv2.IMREAD_COLOR)
    print('--SR SHAPE--')
    print(sr_image.shape)
    # image = np.array(Image.open(stream))
    # sr_image = sr_image[:,:,:1]
    print(len(sr_image.shape))
    stream.close()
    print("----------------------------")
    print(type(image))
    # print(image.shape)
    print(pokemon_model.predict(sr_image))
    val_predict = pokemon_model.predict(sr_image)
    os.remove('test_convert.jpg')
    return {"Predict": val_predict}

@app.post("/files")
async def create_file(file: bytes = File(...)):
    stream = BytesIO(file)
    image = np.array(Image.open(stream))
    stream.close()
    image = 255 - image
    # print(type(image))
    # print(image.shape)
    print(model.predict(image))
    val_predict = int(model.predict(image))
    return {"Predict": val_predict}

# for mockup get file
@app.get("/")
async def main():
    content = """
    <body>
    <form action="/files" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    </body>
    """
    return HTMLResponse(content=content)