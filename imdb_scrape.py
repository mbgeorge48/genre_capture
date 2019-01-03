from bs4 import BeautifulSoup
import requests


def get_page_URL(movie):
    imdb_search_URL = r"https://www.imdb.com/find?q="
    movie = movie.replace(" ", "+")
    processed_URL = imdb_search_URL + movie

    r = requests.get(processed_URL)
    soup = BeautifulSoup(''.join(r.text), features="lxml")
    table = soup.find("table", attrs={"class": "findList"})
    print ('Movie search returned: ' + str(r.status_code))
    # genres =  get_genres(table.find("tr").select('a[href]')[0].get('href'))
    return get_genres(table.find("tr").select('a[href]')[0].get('href'))


def get_genres(path):
    list_of_genres = []
    movie_URL = r"https://www.imdb.com" + path
    r = requests.get(movie_URL)
    soup = BeautifulSoup(''.join(r.text), features="lxml")
    genres = soup.find("div", attrs={"class": "subtext"})
    print ('Movie page returned: ' + str(r.status_code))


    parent = genres.find_all("a")
    parent.pop()  # Removes the last one as that contains the release date
    for element in parent:
        list_of_genres.append(element.text)
    return list_of_genres
