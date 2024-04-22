from datetime import datetime

from ninja import NinjaAPI

exceptApi=NinjaAPI()

class BookAlreadyExistsError(Exception):
    def handBookAlreadyExists(self):
        return  {'status': 403,
                 'message': 'Book Already Exists',
                 'timestamp':str(datetime.now())
                 }

class BookDoesNotExists(Exception):
    def handleBookDoesNotExists(self):
        return {'status':403,
                'message':'Book Does not exists',
                'timestamp':str(datetime.now())
                }




