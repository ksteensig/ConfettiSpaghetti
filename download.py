import requests

class Video:
    def __init__(self, dest, title, src, filename):
        self.dest = dest
        self.title = title
        self.link = src
        self.filename = filename

def download_file(src):
    r = requests.get(src)
    if r.status_code == 200:
        return r.content
    return None

def save_file(dest, title, src, filename, content):
    with open(dest + filename + '.mp4'):
        f.write(content)
    return Video(dest, title, src, filename)

#vid = download_file('./', '(O) ^ (O)', 'https://i.imgur.com/KhOSXiT.mp4')
