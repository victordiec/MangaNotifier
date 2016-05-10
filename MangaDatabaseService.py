import re
import _thread
import threading
import time
from MangaDAO import MangaDAO
from HTMLParser import HTMLParser

class MangaDatabaseService (threading.Thread):

    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.html_parser = HTMLParser()
        self.manga_dao = MangaDAO()
        self.threadID = threadID

    def run(self):
        delay = 3600
        while(True):
            print("Starting Thread:" + self.threadID)
            self.store_in_db()
            time.sleep(delay)


    def store_in_db(self):
        list_size = self.html_parser.list_size
        for item in self.html_parser.parse_mangastream():
            #check if record exists
            if not self.manga_dao.check_if_exist(item):
                self.manga_dao.add_manga(item)
                print(self.html_parser.list_size)
                print(item)


    #def update_db(self):
    #create Thread for updating database
    #manga_database_service1 = MangaDatabaseService(1, "Thread-1", 1)

    #start new threads
    #manga_database_service1.start()


if __name__ == '__main__':

    manga_database_service = MangaDatabaseService("1234")
    manga_database_service.store_in_db()
    manga_database_service.run()
