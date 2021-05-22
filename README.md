# object-detection-api
Project INT491 Deep Learning

## Pre-requisites Install
````
$ brew install python
$ python3 -m pip install --upgrade pip
$ pip install fastapi
$ pip install 'uvicorn[standard]'
````
### Model
ดาวน์โหลด Model [pokemon1.h5](https://drive.google.com/file/d/1GULFqHTxJmq-ZIeuEmifEI4BBhdjLds6/view?usp=sharing) แล้ววางใน folder app
````
object-detection-api/
└── app/
    ├── main.py
    ├── pokemon.py
    ├── pokemon1.h5
    ├── requirements.txt
````
### Environment
````
$ python3 -m venv env
$ . env/bin/activate
$ pip3 install -r app/requirements.txt
````
## Run
Run with environment
````
./env/bin/uvicorn app.main:app --reload
````
Normal Run
````
uvicorn app.main:app --reload
````
## Deploy Project with Docker
Build Image
````
docker build -t obj-api .
````
Run Container
````
$ docker run -d --name obj-api-container -p 8000:8000 obj-api
````
