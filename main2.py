#region
import subprocess
import pafy
import uuid
import json

from flask import Flask, request, send_file, render_template
from uuid import uuid4

#endregion

app = Flask(__name__, template_folder='www') 

def download_mp3(url, download_path):
    return subprocess.call(['youtube-dl', '--cookies C:\\Users\\Administrator\\Desktop\\code\\PYTHON\\YT2MP3\\youtube.txt' ,  '--extract-audio', '--audio-format', 'mp3', '-o', download_path, url])
    #return subprocess.call(['youtube-dl', '--cookies', 'C:\Users\Administrator\Desktop\code\PYTHON\YT2MP3\cookies.txt', '--extract-audio', '--audio-format', 'mp3', '-o', '-f best', download_path, url])
#   'youtube-dl', '--cookies', 'C:\Users\Administrator\Desktop\code\PYTHON\YT2MP3\cookies.txt'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/youtube-url', methods=['GET'])


def youtube_url():
    url = request.args.get('url', '')

     # Get the video from pafy
    video = pafy.new(url)
      # Get the title of the video
    title = video.title

    download_path = './{}.mp3'.format(uuid.uuid4())

    if url:
        download_mp3(url, download_path)
        return send_file(download_path, download_name=''+title+'.mp3'.format(uuid.uuid4()), as_attachment=True)
    else:
        return 'No URL was provided.'

if __name__ == '__main__':
    app.run()
