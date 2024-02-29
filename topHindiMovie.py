from urllib import request
from urllib.request import Request
from bs4 import BeautifulSoup
import json


def soupfunction(url):
    request_site = Request(url,headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})
    html = request.urlopen(request_site).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup



def allLinks():
    urls = []
    myMovies = []
    soup = soupfunction('https://www.imdb.com/list/ls009997493/')
    for i in soup.find_all('a'):
        links = i.get('href')
        urls.append(links)

    urls = ['https://www.imdb.com/' + x.strip() for x in urls if x is not None and x.startswith('/title/tt')]

    [myMovies.append(link) for link in urls if link not in myMovies]
    myMovies = set(myMovies)
    return list(myMovies)


# myMovies =allLinks()
# print(len(myMovies))


def getMovieinfo():
    dataList = []
    myMovies = allLinks()

    for i in myMovies[:50]:
        soup = soupfunction(i)

        title = soup.find("div", {'class': "sc-69e49b85-0 jqlHBQ"}).find("span").text
        rating = soup.find("div", {"class": "sc-bde20123-2 cdQqzc"}).find("span").text
        minimal = soup.find("meta", property="og:image")['content']
        genre = soup.find("div", {"class": "ipc-chip-list__scroller"}).find("span").text
        director = soup.find("div", {'class': "ipc-metadata-list-item__content-container"}).find("a").text



        myData = {
            "Name": title,
            "Director": director,
            "Poster": minimal,
            "Genre": genre,
            "Rating": rating,

        }
        dataList.append(myData)
    # print(dataList)
    jsonfile =open("topHindiMovies.json",'w')
    json.dump(dataList,jsonfile)


# movies_data = getMovieinfo()

if __name__ =="__main__":
    getMovieinfo()

# print(movies_data)
