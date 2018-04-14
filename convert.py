from moviepy.editor import VideoFileClip, concatenate_videoclips
from download import Video

def convert(videos):
    clips = []
    for v in videos:
        clips.append(VideoFileClip(v.dest + "/" + v.filename + ".mp4"))
    output = concatenate_videoclips(clips)
    output.write_videofile(v.dest + "/" + "output.mp4")

'''
def convert(videos):
    path = videos[0].dest
    with open(path + "/videos.txt", "a") as f:
        for v in videos:
            f.write("file " + v.filename)
    subprocess.call("ffmpeg -f concat -i " + path + "/videos.txt -c copy" + path + "/output.mp4")
'''
