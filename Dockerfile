FROM jupyter/scipy-notebook

RUN pip install joblib

COPY train.py ./train.py
COPY inference.py ./inference.py

RUN python3 train.py