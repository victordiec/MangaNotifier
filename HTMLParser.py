from bs4 import BeautifulSoup
import requests
import sys
import re

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
    def parse_manga(self, manga):
        # print(manga["name"])
        html = requests.get(manga["link"]).text
        soup = BeautifulSoup(html, 'html.parser')
        # print(html)

        table_list = soup.find('table', class_ = 'table table-striped')
        chapter_list = []        

        td_list = table_list.find_all('td') 
        a_list = table_list.find_all('a')       

        for a in a_list[1:]:
            # print(a)
            chapter = a.get_text()
            link = a['href']
            chapter_list.append({'name': chapter, 'link': link})

        return chapter_list



    def parse_chapters(self, manga_name, chapters):
        for chapter in chapters:
            html_parser.parse_chapter(manga_name, chapter)
            sys.exit()


    def parse_chapter(self, manga_name, chapter):
        print (manga_name, chapter)
        html = requests.get(chapter["link"]).text
        soup = BeautifulSoup(html, 'html.parser')

        # print(html)
        dl_list = soup.find_all('ul', class_ = 'dropdown-menu')

        page_list = dl_list[2].find_all('li')
        last_page = page_list[-1].get_text()
        # print(last_page)

        match = re.match('Last\s+Page\s+\((\d+)\)', last_page)

        print(chapter["link"])
        link_hdr = (re.match("(http:\/\/(mangastream|readms).com\/r\/[\w\d\_]+\/\d+\.?\d+\/\d+\/)",chapter["link"])).group(1)
        print(link_hdr)

        if match:
            last_page = match.group(1)
            print("This is the last page", last_page)

            for i in range(1,int(last_page)+1):
                print(link_hdr+str(i))

        else:
            print("Couldn't find the last page")



        # print(page_list[-1].get_text())

        sys.exit()


if __name__ == '__main__':
    html_parser = HTMLParser()
    master_manga_list = html_parser.parse_mangastream()

    #Grab XML to determine which mangas to download, and which mangas not to download

    # print(master_manga_list)
    
    for manga in master_manga_list[1:]:
        # print(manga['name'])

        chapters = html_parser.parse_manga(manga)        
        html_parser.parse_chapters(manga['name'], chapters)

