import ffmpy
import subprocess
import io
from download import Video

def convert(videos):
    path = videos[0].dest
    with io.FileIO(dest + "/videos.txt", "wa") as f:
        for v in videos:
            f.write("file " + v.filename)
    subprocess.call("ffmpeg -f concat -i " + dest + "/videos.txt -c copy" + dest + "/output.mp4")
