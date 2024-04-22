from ninja import ModelSchema,Schema

from .models import Book, Favorites

"""
Book Im Schema
model: Book
fields: title,code,author,genre,rating,publisher,price,stock
author:Santhosh  Kumar
Date Created: 06/01/2024
Date modified:

"""
class BookIn(ModelSchema):
    class Meta:
        model=Book
        fields=['title','code','author','genre','rating','publisher','price','stock']


"""
Book Out Schema
model:Book
fields:  title,code,author,genre,rating,publisher,price,stock
author:Santhosh Kumar
Date Created: 06/01/2024
Date Modified:

"""

class BookOut(ModelSchema):
    class Meta:
        model=Book
        fields = ['id','title', 'code', 'author', 'genre', 'rating', 'publisher', 'price', 'stock']

class Error(Schema):
    status:int
    message: str
    timestamp:str

class FavoritesIn(ModelSchema):
    class Meta:
        model=Favorites
        fields='__all__'

class FavoritesOut(ModelSchema):
    class Meta:
        model=Favorites
        fields='__all__'
