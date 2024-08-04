#!/bin/sh
cd /app
# We do this all time to hopefully make things easier when yt-dlp updates...
pip install --no-cache-dir -r requirements.txt
exec "$@"
