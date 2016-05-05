import re
from pymongo import MongoClient
from HTMLParser import HTMLParser


class MangaDAO:

    def __init__(self):
        client = MongoClient()
        self.db = client['manganotifier']

    def add_manga(self, manga):
        self.db.manga.insert_one(manga)

    def get_all_manga(self):
        result = list(self.db.manga.find())
        return result

    def update_manga(self, manga):
        result = self.db.manga.update_many(
            {'name': manga['name']},
            {
                '$set': {
                    'release': manga['release'],
                    'link': manga['link']
                }
            }
        )

if __name__ == '__main__':
    manga_dao = MangaDAO()

    #Add
    #manga_dao.add_manga({'name': 'The Heroic Legend of Arslan', 'release': '10 - A Captured Queen', 'link': 'http://readms.com/r/arslan/10/2417/1'})
    #loop to add all records to db
    html_parser = HTMLParser()

    print(html_parser.parse_mangastream())
    print(html_parser.list_size)



    line = html_parser.parse_mangastream()
    #m = re.search(, line)
