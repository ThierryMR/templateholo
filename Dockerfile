FROM python:3.8-buster

COPY fast.py fast.py
COPY requirements.txt requirements.txt

RUN pip install -U pip
RUN pip install -r requirements.txt

CMD uvicorn fast:app --host 0.0.0.0 --port $PORT