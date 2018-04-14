import ffmpy
import subprocess
import io
from download import Video

def convert(videos):
    path = videos[0].dest
    with io.FileIO(dest + "/videos.txt", "w") as file:
        for v in videos:
            file.write("file " + v.filename)
    subprocess.call("ffmpeg -f concat -i " + dest + "/videos.txt -c copy" + dest + "/output.mp4")
