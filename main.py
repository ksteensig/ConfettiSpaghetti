from download import Video, download_file, save_file
from scrape import extract_links, sub2save
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
    
    return list(videos)

ts = str(time.time()) 

vids = scrape("./funny/" + ts, "funny", 5)
convert(vids)
