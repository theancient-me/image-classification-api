# util
import shutil
import datetime

# fastapi
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/")
def root_welcome():
    return {
        "status": 200,
        "message": "OK"
    }

@app.post("/image")
async def image(image: UploadFile = File(...)):
    time_now = str(datetime.datetime.now().timestamp())
    ftime  = time_now.split('.')
    
    print(type(time_now))
    
    # Writ file into disk
    with open("store/img-"+ftime[0]+".png", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": image.filename}

