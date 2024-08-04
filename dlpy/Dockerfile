FROM python:3.12-alpine
WORKDIR /app

RUN apk add ffmpeg

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#COPY main.py .

COPY entrypoint.sh .
RUN chmod 755 entrypoint.sh

CMD ["/app/entrypoint.sh", "gunicorn", "--workers", "4", "--bind", "0.0.0.0:8888", "main:app"]
