from .exceptions import BookAlreadyExistsError
from .models import Book, Favorites

"""
Converting dictionary to Book Entity
Author:Santhosh Kumar
Date Created: I don't remember
Date Modified: 09/01/2023
"""
def bookDictToEnt(data,book):
    for attr,value in data.items():
        setattr(book,attr,value)
    return book


"""
Checking the existence of the book 
Author: Santhosh Kumar
Date Created: I don't Known
Date Modified: 09/01/2023
"""
def  checkBookExistence(code='',id=0,author='',publisher='',rating=0,genre=''):
        if id!=0:
            book=Book.objects.filter(id=id).values()
        if code!='':
            book = Book.objects.filter(code=code).values()
        if author!='':
            book=Book.objects.filter(author=author).values()
        if publisher!='':
            book=Book.objects.filter(publisher=publisher).values()
        if rating!=0:
            book=Book.objects.filter(rating=rating).values()
        if genre!='':
            book=Book.objects.filter(genre=genre).values()

        if len(book)==0:
            result=False
        elif book[0]['code'] == code or book[0]['id'] or book[0]['author']==author or book[0]['publisher']==publisher or book[0]['rating']==rating or book[0]['genre']==genre:
            result=True
        else:
            result=False
        return result

"""
Filtering out the books within price limit
Author: Santhosh Kumar
Date Created: 09/01/2024
Date Modified:
"""
def filteringByPriceLimit(data,price):
    if data.price<=price:
        return True
    else:
        return False

"""
Checking Favorite
param:FavoriteIn
Author:Santhosh Kumar
Date Created: 18/04/2024
Date Modified:
"""
def checkFavoriteAlreadyExists(data):
    result=False
    favoritesList=Favorites.objects.filter(customerCode=data.customerCode).values()
    favorite=getCustomerFavorite(favoritesList,data)
    if favorite==True:
        result=True
    else:
        result=False
    return result

"""
A subfunction for getting the particualr book of favorites from the list
Author: Santhosh Kumar
Date Created: 18/04/2024
Date Modified:
"""
def getCustomerFavorite(favoritesList,data):
    for i in favoritesList:
        result=dictToFavorite(i,Favorites())
        if result.customerCode==data.customerCode and result.bookCode==data.bookCode :
            return True

"""
Converting Dictionary to Favorite
Author:Santhosh Kumar
Date Created: 18/04/2024
Date Modified:
"""
def dictToFavorite(data,favorite):
    for attr,value in data.items():
        setattr(favorite,attr,value)
    return favorite




