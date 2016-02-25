from pymongo import MongoClient


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
    print(manga_dao.get_all_manga())
