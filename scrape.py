import praw
import itertools as it
import keys

_SORTINGS = ["controversial", "gilded", "hot", "new", "rising", "top"]
_TIMEFILTERS = ["day", "hour", "month", "week", "year", "all"]

def subreddit_iterator(subreddit, sorting="hot", time_filter="all", **generator_kwargs):
    assert(sorting in _SORTINGS)
    assert(time_filter in _TIMEFILTERS)
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
    return sm.url

def extract_redditv(sm):
    return sm.media["reddit_video"]["fallback_url"]

def submission_transform(sm):
    return (sm.title, extract_submission(sm))

def extract_links(subreddit, resultsize = 100, **generator_kwargs):
    return it.islice(filter(lambda sm: sm[1] is not None, map(submission_transform, subreddit_iterator(subreddit, **generator_kwargs))), resultsize)

results = extract_links("funny", limit = None)

for sm in results:
    print(sm)