import get_names
import imdb_scrape
import json

movies_genres = dict()
movie_list = get_names.get_json_names()
print ("Number of titles found: " + str(len(movie_list)))
failed_list = []
i = 0
# for movie in movie_list:
#     i = i + 1
#     print (str(i) + "/" + str(len(movie_list)) + "|  Processing: " + movie)
#     try:
#         movies_genres[movie] = imdb_scrape.get_page_URL(movie)
#     except:
#         print ("Failed: " + movie + "\n")
#         failed_list.append(movie)
#     # print (movie + str(imdb_scrape.get_page_URL(movie)))
# print (len(movies_genres))
# movies_genres['Failed'] = failed_list
# with open('data.json', 'w') as outfile:
#     json.dump(movies_genres, outfile, sort_keys=True, indent=4)



