# util (bank)
import shutil
import datetime
import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()
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
# bank
@app.post("/image")
async def image(image: UploadFile = File(...)):
    time_now = str(datetime.datetime.now().timestamp())
    ftime  = time_now.split('.')
    print(type(time_now))
    # Writ file into disk
    with open("store/img-"+ftime[0]+".png", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": image.filename}

@app.get("/store/list")
async def getlistImage():
    folder = 'store'
    list_img = [];
    for filename in os.listdir(folder):
        list_img.append(filename)
    return {
        'status' : 200,
        'message' : 'OK',
        'data' : list_img
    }