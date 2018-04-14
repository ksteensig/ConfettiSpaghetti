import praw
import itertools as it
import keys
import time
from imgur import imgur_parse_link
from download import download_file

_SORTINGS = ["controversial", "gilded", "hot", "new", "rising", "top"]
_TIMEFILTERS = ["day", "hour", "month", "week", "year", "all"]

def subreddit_iterator(subreddit, sorting="hot", time_filter="all", **generator_kwargs):
    assert sorting in _SORTINGS, "Invalid sorting: %r" % sorting
    assert time_filter in _TIMEFILTERS, "Invalid timefilter: %r" % time_filter
    genfunc = getattr(keys.reddit.subreddit(subreddit), sorting)
    if sorting in ["controversial", "top"]:
        return genfunc(time_filter, **generator_kwargs)
    else:
        return genfunc(**generator_kwargs)

def extract_submission(sm):
    if sm.is_video:
        return extract_redditv(sm)
    elif sm.domain in ["imgur.com", "i.imgur.com"]:
        return extract_imgur(sm)
    else:
        return None

def extract_imgur(sm):
    return imgur_parse_link(sm.url)

def extract_redditv(sm):
    return sm.media["reddit_video"]["fallback_url"]

def submission_transform(sm):
    return (sm.title, extract_submission(sm))

def extract_links(subreddit, resultsize = 100, **generator_kwargs):
    #Force None as default limit
    generator_kwargs["limit"] = generator_kwargs.get("limit")
    return it.islice(filter(lambda sm: sm[1] is not None, map(submission_transform, subreddit_iterator(subreddit, **generator_kwargs))), resultsize)

def sub2save(name, dest, sm):
    return dest, sm[0], sm[1], name, download_file(sm[1])

results = extract_links("wholesomememes", resultsize = 10)

for sm in results:
    print(sm)