from typing import Optional
from app.mnist import PredictImage
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from PIL import Image
from io import BytesIO
import numpy as np


app = FastAPI()
model = PredictImage("./app/my_model.h5")

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