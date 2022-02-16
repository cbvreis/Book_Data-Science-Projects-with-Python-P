#CREATE DOCKER FIULE FROM PYTHON3.7 ALPINE
FROM jupyter/scipy-notebook
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
