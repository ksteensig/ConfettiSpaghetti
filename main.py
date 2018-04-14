from download import Video, download_file, content_type
from scrape import subreddit_iterator, extract_submission

def scrape(subreddit)
    urls = []
    vids = [] 

    for u in urls:
        v = download_file('./' + subreddit, u[0], u[1])
        vids.append(v)
    
    return vids 
