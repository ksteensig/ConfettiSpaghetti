import moviepy.editor as mp
from moviepy.video.fx import resize
from download import Video

def convert(videos, sounds, dest, tduration = 30):
    acc = 0
    clips = []
   
    for v, s in zip(videos, sounds):
        c = process_clip(v, s)
        acc += c.duration
        clips.append(c)
        if acc > tduration:
            break
    
    output = mp.concatenate_videoclips(clips, method="compose")
    output.write_videofile(dest + "/" + "output.mp4")

def process_clip(video, sound):
    base_clip = mp.VideoFileClip(video.dest + "/" + video.filename + ".mp4")
    base_clip = resize.resize(base_clip, width=640, height=480)
    title_clip = mp.TextClip(sound.title, fontsize=50, color="white", font="arial", method="caption", size=(base_clip.size[0],None))
    title_clip = title_clip.on_color(size=(title_clip.size[0] + 10,title_clip.size[1] + 10), col_opacity=0.5).set_duration(3).set_position("center")
    comment_clip = mp.TextClip(sound.top_comment, fontsize=20, color="white", method="caption", size=(base_clip.size[0],None)).on_color(col_opacity=0.5)
    comment_clip = comment_clip.set_duration(3).set_start(base_clip.duration / 2).set_position("bottom")


    title_tts = mp.AudioFileClip(sound.dest + "/title" + sound.filename + ".mp3").set_start(0)
    comment_tts = mp.AudioFileClip(sound.dest + "/comment" + sound.filename + ".mp3").set_start(base_clip.duration / 2)

    audio = mp.CompositeAudioClip([title_tts, comment_tts])

    clip = mp.CompositeVideoClip([base_clip, title_clip, comment_clip])
    return clip.set_audio(audio)

'''
def convert(videos):
    path = videos[0].dest
    with open(path + "/videos.txt", "a") as f:
        for v in videos:
            f.write("file " + v.filename)
    subprocess.call("ffmpeg -f concat -i " + path + "/videos.txt -c copy" + path + "/output.mp4")
'''
