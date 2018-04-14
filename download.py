import requests
from time import sleep
import os
import errno
import io

class Video:
    def __init__(self, dest, title, src, filename):
        self.dest = dest
        self.title = title
        self.link = src
        self.filename = filename

def download_file(src):
    print("Now downloading: %r" % src)
    for i in range(1,100):
        r = requests.get(src)
        if r.status_code == 200:
            return r.content
        sleep(0.1)
    assert False, "Could not download: %r" % src

def save_file(dest, title, src, filename, content):
    fp = dest + '/' + filename + '.mp4'
    os.makedirs(os.path.dirname(fp), exist_ok=True) 
    with io.FileIO(fp, "wb") as f:
        f.write(content)
    return Video(dest, title, src, filename)

#vid = download_file('./', '(O) ^ (O)', 'https://i.imgur.com/KhOSXiT.mp4')
