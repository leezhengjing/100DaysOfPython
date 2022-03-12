from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")
movies = soup.find_all(name="h3", class_="title")
titles = []
for movie in movies:
    titles.append(movie.getText())
titles = titles[::-1]
print(titles)

with open("movies.txt", mode="w") as file:
    file.write("\n".join(titles))
