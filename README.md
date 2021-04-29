# object-detection-api
Project INT491 Deep Learning

## Run Project with Local
### Pre-requisites Install
````
$ brew install python
$ /Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9 -m pip install --upgrade pip
$ pip install fastapi
$ pip install 'uvicorn[standard]'
````
### Run
````
$ uvicorn app.main:app --reload
````

## Deploy Project with Docker
````
Build Image
$ docker build -t myimage .
Run Container
$ docker run -d --name mycontainer -p 80:80 myimage
````
