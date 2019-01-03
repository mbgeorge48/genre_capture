import requests
from bs4 import BeautifulSoup
import json
import sys


def get_json_names():
    netflix_URL = r"https://www.netflix.com/browse/genre/34399"
    r = requests.get(netflix_URL)

    soup = BeautifulSoup(''.join(r.text), features="lxml")

    for link in soup.find_all('script'):
        if link.get('type') != None:
            if 'application/ld+json' in link.get('type'):
                data = link.string
                break
            else:
                data = 'No json found'
                sys.exit

    json_data = json.loads(data)
    movie_list = []
    for pos in json_data["itemListElement"]:
        if pos["item"]["name"] not in movie_list:
            movie_list.append(pos["item"]["name"])
    print ('Netflix returned: ' + str(r.status_code))
    return movie_list
