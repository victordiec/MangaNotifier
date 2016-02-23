from bs4 import BeautifulSoup
import requests

"""
Urls currently being scraped:

http://mangastream.com/manga

"""



"""
Class: HTMLParser

Description:

This class is used to parse the different manga websites in order to obtain
a list of mangas, the newest release, and the link to the release.

Methods should return an array containing dictionaries:

[
    {
        "name": <manga name>,
        "release": <release>,
        "link": <link>
    },
    ...
    ...
    ...
]

"""

class HTMLParser:

    def parse_mangastream(self):
        html = requests.get('http://mangastream.com/manga').text
        soup = BeautifulSoup(html, 'html.parser')
        table_list = soup.find('table', class_ = 'table table-striped')
        tr_list = table_list.find_all('tr')

        manga_list = []

        for tr in tr_list[1:]:
            td_list = tr.find_all('td')
            manga = td_list[0].find('strong').find('a').get_text()
            release = td_list[1].find('a', class_ = 'chapter-link').get_text()
            link = td_list[1].find('a', class_ = 'chapter-link')['href']
            manga_list.append({'name': manga, 'release': release, 'link': link})

        return manga_list


if __name__ == '__main__':
    html_parser = HTMLParser()
    print(html_parser.parse_mangastream())
