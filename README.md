# Pokemon Classification
โปรแกรม Pokemon Classification เป็นเว็บแอปพลิเคชันที่จำลองเครื่อง Pokedex ซึ่งเป็นเครื่องที่ช่วยบอกข้อมูลเกี่ยวกับโปเกมอนเนื่องจากโปเกมอนมีมากถึง 898 สายพันธุ์ ทำให้ยากต่อการจดจำว่าแต่ละสายพันธุ์ชื่ออะไร โปรแกรมนี้จะช่วยให้ผู้ใช้สามารถจำแนกประเภทข้อมูลภาพ (Image Classification) ของโปเกมอนว่าแต่ละภาพคือสายพันธุ์อะไร โดยใช้เทคโนโลยี Deep Learning ซึ่งเป็นส่วนหนึ่งของ Machine Learning มาเรียนรู้และจำแนกประเภทของโปเกมอน 150 สายพันธุ์

ดาวน์โหลด Front-end ได้ที่ [image-classification-frontend](https://github.com/theancient-me/vue-object-detection)

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

## About us
เว็บแอปพลิเคชันนี้เป็นส่วนหนึ่งของวิชา INT491 Applied Deep Learning ภาคเรียนที่ 2 ปีการศึกษา 2563 คณะเทคโนโลยีสารสนเทศ มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าธนบุรี
### ผู้จัดทำ
- นาย จตวัฒน์	    เซี่ย			รหัสนักศึกษา 60130500009
- นาย จิรพันธ์    เย็นขัน			รหัสนักศึกษา 60130500012
- นาย ฐณพล	ประดิษฐ์สถบดี		รหัสนักศึกษา 60130500024
### อาจารย์ผู้สอน
ผศ.ดร. สายชล ใจเย็น
