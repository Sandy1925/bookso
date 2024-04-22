from typing import Union

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ninja import NinjaAPI
from typing import List
from .exceptions import BookAlreadyExistsError, BookDoesNotExists
from .models import Book, Favorites
from .schemas import BookIn, BookOut, Error, FavoritesOut, FavoritesIn
from .services import bookDictToEnt, checkBookExistence, filteringByPriceLimit, checkFavoriteAlreadyExists, \
    dictToFavorite

api=NinjaAPI()


"""
Adding new Book to the table
params: BookIn
author: Santhosh Kumar
Date Created: 06/01/2024
Date Modified:
"""
@api.post("newBook",response={200:BookOut,403:Error})
def newBook(request,data:BookIn):
    try:
             if checkBookExistence(code=data.code)==True :
                 raise BookAlreadyExistsError
             else:
                 book = Book()
                 result = bookDictToEnt(data.dict(), book)
                 result.save()
                 return 200, result
    except BookAlreadyExistsError as b :
        error=b.handBookAlreadyExists()
        return 403,error


"""
Get Book By Code
param: code
author: Santhosh Kumar
Date Created: 08/01/2024
Date Modified:
"""
@api.get("getByCode/{code}", response={200: BookOut,403:Error})
def getByCode(request,code:str):
    try:
        if checkBookExistence(code=code)== False:
            raise BookDoesNotExists
        else:
            data = Book.objects.filter(code=code).values()
            book = Book()
            result = bookDictToEnt(data[0], book)
            return 200,result
    except BookDoesNotExists as be:
        error=be.handleBookDoesNotExists()
        return 403,error

"""
Getting book by id
Author: Santhosh Kumar
Date Created: 09/01/2024
"""
@api.get("getById/{id}",response={200:BookOut, 403: Error})
def getBookById(request,id:int):
    try:
       if checkBookExistence(id=id)==False:
           raise BookDoesNotExists
       else:
           data=Book.objects.filter(id=id).values()
           book=Book()
           result=bookDictToEnt(data[0],book)
           return 200,result
    except BookDoesNotExists as be:
        error=be.handleBookDoesNotExists()
        return 403,error

"""
Getting all the books
Author:Santhosh Kumar
Date Created: 09/01/2024
Date Modified:
"""
@api.get("getAll",response=List[BookOut])
def getAllBooks(request):
    data=Book.objects.all()
    return data

"""
Getting books by author
Author: Santhosh Kumar
Date Created: 09/03/2024
Date Modified:
"""
@api.get("getAllByAuthor/{author}",response={200:List[BookOut],403:Error})
def getAllByAuthor(request,author:str):

    try:
        if checkBookExistence(author=author)==False:
            raise BookDoesNotExists
        else:
            data=Book.objects.filter(author=author).values()
           # book=Book()
            result = list(map(lambda b: bookDictToEnt(b, Book()), data))
            return 200,result
    except BookDoesNotExists as be:
        error=be.handleBookDoesNotExists()
        return 403,error

"""
Get Books by Publisher
Author:Santhosh Kumar
Date Created: 09/01/2024
Date modified:
"""
@api.get("getAllByPublisher/{publisher}",response={200:List[BookOut],403:Error})
def getAllByPublisher(request,publisher:str):
    try:
        if checkBookExistence(publisher=publisher)==False:
            raise BookDoesNotExists
        else:
            data=Book.objects.filter(publisher=publisher).values()

            result = list(map(lambda b: bookDictToEnt(b, Book()), data))
            return 200,result
    except BookDoesNotExists as be:
        error=be.handleBookDoesNotExists()
        return 403,error

"""
Getting Books by rating
Author: Santhosh Kumar
Date Created: 09/01/2024
Date Modified:
"""
@api.get("getAllByRating/{rating}",response={200:List[BookOut],403:Error})
def getAllByRating(request,rating:int):
    try:
        if checkBookExistence(rating=rating)==False:
            raise BookDoesNotExists
        else:
            data=Book.objects.filter(rating=rating).values()

            result=list(map(lambda b: bookDictToEnt(b,Book()),data))
            return 200,result
    except BookDoesNotExists as be:
        error=be.handleBookDoesNotExists()
        return 403,error

"""
Get all Books by genre
Author :Santhosh Kumar
Date Created: 09/01/2024
Date modified;
"""
@api.get("getAllByGenre/{genre}",response={200:List[BookOut],403:Error})
def getAllByGenre(request,genre:str):

    try:
        if checkBookExistence(genre=genre)==False:
            raise BookDoesNotExists
        else:
            data=Book.objects.filter(genre=genre).values()
            result=list(map(lambda b: bookDictToEnt(b,Book()),data))
            return 200,result
    except BookDoesNotExists as be:
        error=be.handleBookDoesNotExists()
        return 403,error

"""
Get Book within a price limit
Author: Santhosh Kumar
Date Created: 09/01/2024
Date Modified:
"""
@api.get("getAllByPriceLimit/{priceLimit}",response=List[BookOut])
def getByPriceLimit(request,priceLimit:float):
    data=Book.objects.all()
    result=filter(lambda b:filteringByPriceLimit(b,priceLimit),data)
    return result

"""
Updating a book by using code
Author: Santhosh kumar
Date Created: 09/01/2024
Date modified:
"""
@api.post("/updateBook/{code}",response={200:BookOut,403:Error})
def updateBook(request,code:str,data:BookIn):
    try:
       if checkBookExistence(code=code)==False:
           raise BookDoesNotExists
       else:
           bookSet = Book.objects.filter(code=code).values()
           book = bookDictToEnt(bookSet[0], Book())
           result = bookDictToEnt(data.__dict__, book)
           result.save()
           return 200,result
    except BookDoesNotExists as be:
        error = be.handleBookDoesNotExists()
        return 403, error

"""
Deleting Book By Id
Author:Santhosh kumar
Date Created: 09/01/2024
Date Modified:
"""
@api.delete("deleteBook/{id}")
def deleteBook(request,id:int):
    book=Book.objects.get(id=id)
    book.delete()
    return {200:"Deleted successfully"}


"""
Adding a Favorite Book
Author:Santhosh Kumar
Date Created: 18/04/2024
Date Modified:
"""
@api.post("addFavorite",response=FavoritesOut)
def addToFavorite(request,data:FavoritesIn):
    result = dictToFavorite(data.__dict__, Favorites())
    if not(checkFavoriteAlreadyExists(data)):
        result.save()
        return result
    else:
        return result

"""
Getting all Favorites
Author:Santhosh Kumar
Date Created: 18/04/2024
Date Modified:
"""
@api.get("getMyFavs/{customerCode}",response=List[FavoritesOut])
def getAllFavorites(request,customerCode:str):
    favoritesList=Favorites.objects.filter(customerCode=customerCode).values()
    result=list(map(lambda b:dictToFavorite(b,Favorites()),favoritesList))
    return result






























