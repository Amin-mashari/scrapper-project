FROM python:3.9.13-slim

COPY . /app

WORKDIR /app

RUN pip install -r requrements.txt

ENTRYPOINT [ "python" , "main.py" ]