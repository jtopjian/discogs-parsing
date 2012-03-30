from BeautifulSoup import BeautifulSoup
import requests
import re

def style_search(data, styles):
    """ Given a dataset of discog data and an array
        of styles, this function will return all
        releases with all given styles

    """
    results = []
    for k in data:
        found = 1
        curr_data = data[k]
        style = curr_data.get('style',['none'])
        if style[0] == 'none':
            continue
        for s in styles:
            if s not in [x.lower() for x in style]:
                found = 0
        if found:
            results.append(k)
    return results

def get_rating(release_id):
    """ Given a discogs release id, this will return the
        rating of the release as a tuple:
        rating / number of votes

    """
    URL = "http://www.discogs.com/release"
    url = "%s/%s" % (URL, release_id)
    try:
        r = requests.get(url)
    except:
        print "Unable to access %s" % url

    soup = BeautifulSoup(r.text)
    rating = soup.findAll('span', attrs={'class': re.compile('rating_value')})[0]
    count = soup.findAll('span', attrs={'class': re.compile('rating_count')})[0]

    return (rating.text, count.text)
