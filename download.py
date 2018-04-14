import requests

#content_type = ['.mp4', '.gifv', '.webm']

class Video:
    def __init__(self, dest, title, src):
        self.dest = dest
        self.title = title
        self.link = src
        self.filename = title.replace(' ', '')

def download_file(dest, title, src):
    r = requests.get(src)
    if r.status_code == 200:
        vid = Video(dest, title, src, ct)
        with open(dest + title.replace(' ', '') + ct, 'wb') as f:
            f.write(r.content)
        return vid
    return None

#vid = download_file('./', '(O) ^ (O)', 'https://i.imgur.com/KhOSXiT.mp4')