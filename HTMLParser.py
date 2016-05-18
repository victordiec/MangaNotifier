from bs4 import BeautifulSoup
import requests

"""
Urls currently being scraped:

http://mangastream.com/manga

"""



"""
Class: HTMLParser

Description:

This class is used to find all the different manga currently being scanlated by
Mangastream, keep track of them in a local XML file and set to run automatically
using cron so no updates are ever missed

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
    def __init__(self):
        self.list_size = 0

    def parse_mangastream(self):

        #Gets all the html from a page
        html = requests.get('http://mangastream.com/manga').text

        #Makes it easier to parse
        soup = BeautifulSoup(html, 'html.parser')

        #Find all the code in the table attribute/tag
        table_list = soup.find('table', class_ = 'table table-striped')
        
        # #Find all the code with the links tr
        # tr_list = table_list.find_all('tr')

        manga_list = []

        # for tr in tr_list[1:]:
        #     td_list = tr.find_all('td')
        #     manga = td_list[0].find('strong').find('a').get_text()

        #     release = td_list[1].find('a', class_ = 'chapter-link').get_text()
        #     link = td_list[1].find('a', class_ = 'chapter-link')['href']
        #     manga_list.append({'name': manga, 'release': release, 'link': link})

        # self.list_size = len(manga_list)

        # #List of manga
        #     #link       - link to the first page
        #     #release    - name of the most recent chapter
        #     #name       - name of the manga
        # return manga_list

        strong_list = table_list.find_all('strong')

        for strong in strong_list[1:]:
            a = strong.find('a')
            manga = a.get_text()
            link = a['href']
            manga_list.append({'name': manga, 'link': link})


        return manga_list


    # This is because most methods do some work with the object they're called on,
    # so there needs to be some way for that object to be referred to inside the method.
    # By convention, this first argument is called self inside the method definition:
    def parse_manga(self, manga_link ):
        print(manga_link)



if __name__ == '__main__':
    html_parser = HTMLParser()
    master_manga_list = html_parser.parse_mangastream()

    # print(master_manga_list)
    
    for manga in master_manga_list[1:]:
        # print(manga)
        html_parser.parse_manga(manga)
