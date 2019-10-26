FROM python:3.7-slim-buster

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app"
CMD ["python", "cloudwall/serenity/mdrecorder/scheduler.py"]