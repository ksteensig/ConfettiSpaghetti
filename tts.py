from gtts import gTTS

class TextToSpeech:
    def __init__(self, dest, filename, title, top_comment):
        self.dest = dest
        self.filename = filename
        self.title = title
        self.top_comment = top_comment

def tts(dest, filename, title, top_comment):
    title_tts = gTTS(text=title, lang='en')
    top_comment_tts = gTTS(text=top_comment, lang='en')
    title_tts.save(dest + "/title" + filename + ".mp3")
    top_comment_tts.save(dest + "/comment" + filename + ".mp3")

    return TextToSpeech(dest, filename, title, top_comment)    
