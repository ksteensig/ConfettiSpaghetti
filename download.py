import requests
from time import sleep

class Video:
    def __init__(self, dest, title, src, filename):
        self.dest = dest
        self.title = title
        self.link = src
        self.filename = filename

def download_file(src):
    for i in range(1,100):
        r = requests.get(src)
        if r.status_code == 200:
            return r.content
        sleep(0.1)
    assert False, "Could not download: %r" % src

def save_file(dest, title, src, filename, content):
    with open(dest + '/' + filename + '.mp4',"w") as f:
        f.write(content)
    return Video(dest, title, src, filename)

#vid = download_file('./', '(O) ^ (O)', 'https://i.imgur.com/KhOSXiT.mp4')
