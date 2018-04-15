import moviepy.editor as mp
from moviepy.video.fx import resize, fadein, loop
from moviepy.audio.fx import volumex, audio_loop
from download import Video

def convert(videos, sounds, dest, tduration = 30, mduration = 30):
    acc = 0
    clips = []
   
    for v, s in zip(videos, sounds):
        c = read_clip(v)
        if c.duration >= mduration:
            continue
        c = process_clip(c, s)
        acc += c.duration
        clips.append(c)
        if acc > tduration:
            break

    end_clip = mp.TextClip("FIN", fontsize=100, color="white", font="garamond", method="caption").set_duration(3)
    clips.append(end_clip)

    output = mp.concatenate_videoclips(clips, method="compose")
    music = audio_loop.audio_loop(volumex.volumex(mp.AudioFileClip("bgm.mp3").set_start(0), 0.2),
                                  duration=output.duration)

    new_audio = mp.CompositeAudioClip([music, output.audio])
    output = output.set_audio(new_audio)
    output.write_videofile(dest + "/" + "output.mp4")

def read_clip(video):
    return mp.VideoFileClip(video.dest + "/" + video.filename + ".mp4", audio=False)

def process_clip(clip, sound):
    base_clip = clip
    base_clip = resize.resize(base_clip, width=640, height=480)
    title_tts = mp.AudioFileClip(sound.dest + "/title" + sound.filename + ".mp3").set_start(0)
    title_clip = mp.TextClip(sound.title, fontsize=50, color="white", font="garamond", method="caption", size=(base_clip.size[0],None))
    title_clip = title_clip.on_color(size=(title_clip.size[0] + 10,title_clip.size[1] + 10), col_opacity=0.5).set_duration(title_tts.duration).set_position("center")
    title_clip = fadein.fadein(title_clip, 0.2, (255, 255, 255))

    comment_tts = mp.AudioFileClip(sound.dest + "/comment" + sound.filename + ".mp3")
    comment_time = max(min(base_clip.duration - comment_tts.duration, base_clip.duration / 2), title_tts.duration + 1)
    comment_clip = mp.TextClip(sound.top_comment, fontsize=20, color="white", method="caption", size=(base_clip.size[0],None)).on_color(col_opacity=0.5)
    comment_clip = comment_clip.set_duration(comment_tts.duration).set_start(comment_time).set_position("bottom")
    comment_clip = fadein.fadein(comment_clip, 0.2, (255, 255, 255))
    comment_tts = comment_tts.set_start(comment_time)

    audio = mp.CompositeAudioClip([title_tts, comment_tts])
    base_clip = loop.loop(base_clip, duration=max(base_clip.duration, audio.duration + 1))
    newclip = mp.CompositeVideoClip([base_clip, title_clip, comment_clip])
    return newclip.set_audio(audio)

'''
def convert(videos):
    path = videos[0].dest
    with open(path + "/videos.txt", "a") as f:
        for v in videos:
            f.write("file " + v.filename)
    subprocess.call("ffmpeg -f concat -i " + path + "/videos.txt -c copy" + path + "/output.mp4")
'''
