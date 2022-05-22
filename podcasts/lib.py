import re

NO_HTML_RE = re.compile('<.*?>')

def get_clean_podcast_attr(podcast_attr):
    if not podcast_attr:
        return

    clean_podcast_attr = str(podcast_attr).strip()
    clean_podcast_attr = re.sub(NO_HTML_RE, '', clean_podcast_attr)
    return clean_podcast_attr