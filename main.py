from download import Video, download_file, save_file
from prawcore import exceptions as prawex
from tts import tts
from scrape import extract_links, sub2save, sub2sound
from convert import convert
from keys import reddit
import re
import itertools as it
from operator import itemgetter
from datetime import datetime

def scrape(dest, subreddit, **generator_kwargs):
    videos = []

    links = extract_links(subreddit, **generator_kwargs)

    subs = zip(map(str, it.count()), it.repeat(dest), links)

    splitsubs = it.tee(subs)

    saves = it.starmap(sub2save, splitsubs[0])

    videos = it.starmap(save_file, saves)

    texts = it.starmap(sub2sound, splitsubs[1])

    sounds = it.starmap(tts, texts)

    convert(videos, sounds, dest)

def basic_scrape(subreddit):
    ts = str(datetime.now())
    scrape("./" + subreddit + "/" + ts, subreddit)

def user_interface():
    subreddit = None
    print("Welcome to Viddit!")
    while True:
        print("Please enter the name of the subreddit you wish to compile or type 'exit':")
        subreddit = input("> ")
        if subreddit == "exit":
            return
        subreddit = re.sub(r'^r\/', '', subreddit)
        try:
            results = reddit.subreddits.search_by_name(subreddit, include_nsfw=False, exact=True)
        except prawex.NotFound:
            print("Sorry, that subreddit doesn't exist")
            continue
        if not results:
            print("Sorry, that subreddit isn't safe for children ages 6 or under.")
        break

    print("Great! Now let Python do its magic. This might take a while...")
    basic_scrape(subreddit)

user_interface()