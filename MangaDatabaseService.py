import re
from MangaDAO import MangaDAO
from HTMLParser import HTMLParser

class MangaDatabaseService:

    def __init__(self):
        self.html_parser = HTMLParser()
        self.manga_dao = MangaDAO()

    def store_in_db(self):
        list_size = self.html_parser.list_size
        for item in self.html_parser.parse_mangastream():
            #check if record exists
            if not self.manga_dao.check_if_exist(item):
                self.manga_dao.add_manga(item)
                print(self.html_parser.list_size)
                print(item)

    

    #def update_db(self):




if __name__ == '__main__':

    manga_database_service = MangaDatabaseService()
    manga_database_service.store_in_db()
