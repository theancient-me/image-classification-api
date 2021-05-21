# object-detection-api
Project INT491 Deep Learning

## Pre-requisites Install
````
$ brew install python
$ python3 -m pip install --upgrade pip
$ pip install fastapi
$ pip install 'uvicorn[standard]'
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
$ docker build -t myimage .
Run Container
$ docker run -d --name mycontainer -p 8000:8000 myimage
````
