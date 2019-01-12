import get_names
import imdb_scrape
import json
import os
from pathlib import Path

movies_genres = dict()
# movie_list = get_names.get_json_names()
# print ("Number of titles found: " + str(len(movie_list)))
movie_list = list()

with open('test') as my_file:
    for line in my_file:
        movie_list.append(line.replace('/\n', ''))

failed_list = []
i = 0
for movie in movie_list:
    i = i + 1
    print (str(i) + "/" + str(len(movie_list)) + "| Processing: " + movie)
    try:
        movies_genres[movie] = imdb_scrape.get_page_URL(movie)
    except:
        print ("Failed: " + movie + "\n")
        failed_list.append(movie)

if len(failed_list) > 0:
    movies_genres['Failed'] = failed_list


path = '/Development/test_ground/'
genre_list = set()
for movie in movies_genres.items():
    for genre in movie[1]:
        genre_list.add(genre)
        if not os.path.isdir(path + genre):
            print ('Creating shortcut folder -> ' + path + genre)
            os.mkdir(path+genre)
        shortcut = (path + genre + '/' + movie[0])
        if not os.path.exists(shortcut):
            # open((path + genre + '/' + movie[0]), 'a')
            # os.mknod(path + genre + '/' + movie[0])
            file = open(path+genre+'/test', 'w')
            file = open(shortcut.replace('/\n', ''), 'w')
    print ('Created shortcuts for ' + movie[0])


with open('data.json', 'w') as outfile:
    json.dump(movies_genres, outfile, sort_keys=True, indent=4)