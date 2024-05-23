FROM tiangolo/uvicorn-gunicorn:python3.8-slim

WORKDIR /

COPY ./requirements.txt /requirements.txt


RUN pip install -r /requirements.txt \
    && rm -rf /root/.cache/pip

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
    

COPY . .