from __future__ import unicode_literals
import youtube_dl, sys, ffmpeg

audio = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

video = {
    'format': 'bestvideo+bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4'
    }],
}

formato = audio
url = ''

# Selector de formato y URL
if len(sys.argv) > 2:
    url = sys.argv[2]

    if sys.argv[1] == 'audio':
        formato = audio
    elif sys.argv[1] == 'video':
        formato = video
    else:
        print('Formato no válido')

elif len(sys.argv) > 1:
    url = sys.argv[1]
else:
    print("Indica URL del video como parámetro")

# Descarga del video/audio
with youtube_dl.YoutubeDL(formato) as ydl:
    if url != '':
       ydl.download([url])