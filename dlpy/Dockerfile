FROM python:trixie
WORKDIR /app

RUN apt update -y && apt install -y ffmpeg

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#COPY main.py .

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8888", "main:app"]
