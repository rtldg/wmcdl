FROM python:3.12-alpine
WORKDIR /app

RUN apk add ffmpeg

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#COPY main.py .

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8888", "main:app"]
