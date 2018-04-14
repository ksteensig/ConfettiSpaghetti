from download import Video, download_file, save_file
from scrape import extract_links, sub2save
import itertools as it
from operator import itemgetter

def scrape(dest, subreddit, resultsize = 100, **generator_kwargs):
    videos = []

    links = extract_links(subreddit, resultsize, **generator_kwargs)

    subs = zip(map(str, it.count()), it.repeat(dest), links)

    saves = map(sub2save, *subs)

    videos = map(save_file, *saves)
    
    return videos