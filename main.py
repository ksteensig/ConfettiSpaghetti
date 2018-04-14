from download import Video, download_file, save_file
from tts import tts
from scrape import extract_links, sub2save, sub2sound
from convert import convert
import itertools as it
from operator import itemgetter
import time

def scrape(dest, subreddit, resultsize = 5, **generator_kwargs):
    videos = []

    links = extract_links(subreddit, resultsize, **generator_kwargs)

    subs = zip(map(str, it.count()), it.repeat(dest), links)

    saves = it.starmap(sub2save, subs)

    videos = it.starmap(save_file, saves)

    texts = it.starmap(sub2sound, subs)

    sounds = it.starmap(tts, texts)

    return videos, sounds, dest

ts = str(time.time())

vids, snds, dest = scrape("./cats/" + ts, "cats", 3)
convert(vids, snds, dest)
