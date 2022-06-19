# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 19:49:29 2022

"""

def Reverse(lst):
    
    modified_list = lst[::-1]
    return (modified_list)

from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

website = response.text
soup = BeautifulSoup(website , "html.parser")

find_movie = soup.find_all(name = "h3",class_="title")
movie_list = []

for movie in find_movie:
    
    movie_name = movie.getText()
    movie_list.append(movie_name)


reversed_list = Reverse(movie_list)
print(reversed_list)


with open("movies.txt","w") as file:
    for data in reversed_list:
        file.write(data)
        file.write("\n")
