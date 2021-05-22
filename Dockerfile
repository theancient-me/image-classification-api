FROM python:3.9.1

COPY . /app
WORKDIR /app
RUN pip install -r app/requirements.txt

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]