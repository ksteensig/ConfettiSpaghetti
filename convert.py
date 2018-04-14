import moviepy.editor as mp
from moviepy.video.fx import resize
from download import Video

def convert(videos, sounds, dest):
    acc = 0
    clips = []
   
    for v in videos:
        c = process_clip(v)
        acc += c.duration
        clips.append(c)
        if acc > 600:
            break
    
    output = mp.concatenate_videoclips(clips, method="compose")
    output.write_videofile(dest + "/" + "output.mp4")

def process_clip(video):
    base_clip = mp.VideoFileClip(video.dest + "/" + video.filename + ".mp4")
    base_clip = resize.resize(base_clip, width=640, height=480)
    txt_clip = mp.TextClip(video.title, fontsize=50, color="white", font="arial", method="caption", stroke_color="black", stroke_width=1.5, size=(base_clip.size[0],None))
    txt_clip = txt_clip.set_duration(3).set_position("center")

    title_tts = mp.AudioFileClip(video.dest + "/title" + video.filename + ".mp3").set_start(0)
    comment_tts = mp.AudioFileClip(video.dest + "/comment" + video.filename + ".mp3").set_start(base_clip.duration / 2)

    audio = mp.CompositeAudioClip([title_tts, comment_tts])

    clip = mp.CompositeVideoClip([base_clip, txt_clip])
    return clip.set_audio(audio)

'''
def convert(videos):
    path = videos[0].dest
    with open(path + "/videos.txt", "a") as f:
        for v in videos:
            f.write("file " + v.filename)
    subprocess.call("ffmpeg -f concat -i " + path + "/videos.txt -c copy" + path + "/output.mp4")
'''
