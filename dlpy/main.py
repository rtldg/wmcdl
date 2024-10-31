# SPDX-License-Identifier: WTFPL

import sys
import os
import subprocess
from pathlib import Path

from flask import Flask,request
import yt_dlp

app = Flask(__name__)

def get_media_duration(filename):
    print(f'attempting to ffprobe {filename}', file=sys.stderr)
    try:
        r = subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', filename])
        return float(r.decode('utf-8'))
    except:
        print('get_media_duration failed...', file=sys.stderr)
        return 0.0

def ss_media(filename, startat):
    print(f'attempting to start media at {startat}', file=sys.stderr)
    try:
        tempf = Path(filename)
        tempf = tempf.with_name('TEMP'+tempf.name)
        # ffmpeg -ss NUMBER -i FILE -map 0 -c copy out
        r = subprocess.check_output(['ffmpeg', '-ss', str(int(startat)), '-i', filename, '-map', '0', '-c', 'copy', tempf.as_posix()])
        os.replace(tempf, filename)
    except:
        print('ss_media failed...', file=sys.stderr)
        pass

@app.route('/GAOGAOGAO', methods=['POST'])
def download_as_mp3():
    url = request.form['url']
    startat = request.form.get('startat')
    try:
        _ = int(startat)
    except:
        startat = None
    print(f'startat = {startat}', file=sys.stderr)
    #for k in request.form:
    #    print(f'\'{k}\' = \''+request.form[k]+'\'')
    print(f'hello with {url}', file=sys.stderr)

    last_filename = ''
    last_title = ''

    def my_hook(d):
        nonlocal last_filename
        nonlocal last_title
        if d['status'] == 'finished':
            last_filename = d['filename'].rsplit('.', 1)[0] + '.ogg'
            last_title = d['info_dict']['uploader'] + ' - ' + d['info_dict']['title']
            print(f'last_filename = {last_filename} | last_title = {last_title}', file=sys.stderr)
    # yt-dlp.exe --format bestaudio --extract-audio --audio-format ogg <url>
    # https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L214
    ydl_opts = {
        'keepvideo': True, # stop redownloading so much sometimes...
        'format': 'ogg/bestaudio/best',
        'outtmpl': '[%(id)s].%(ext)s',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'vorbis',
        }],
        'paths': {
            'home': '/public_html/media/',
        },
        'progress_hooks': [my_hook],
    }

    # https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#embedding-yt-dlp
    # TODO: Pick a random IPV6 'source_address' for ydl_opts
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(url)
    if error_code == 0:
        url_path = last_filename
        if not (startat is None):
            ss_media(last_filename, startat)
            url_path += f'#t={startat}s'
        j = {
            'OriginalUrlFromForm': url,
            'URL': request.host_url + url_path.removeprefix('/public_html/'),
            'Title': last_title,
            'Duration': get_media_duration(last_filename),
        }
        print(j, file=sys.stderr)
        return j, 200
    else:
        # POST to discord webhook.
        return '', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
