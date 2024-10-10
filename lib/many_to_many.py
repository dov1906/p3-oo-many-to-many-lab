class Author:
    
    def __init__(self, name):
        self.name = name
        self._contracts = []
        self._books = []
        self._royalties = 0
        
    def contracts(self):
        return self._contracts

    def books(self):
        return self._books
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, f"{date}", royalties)
    
    def total_royalties(self):
        return self._royalties
        

class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []
        self._authors = []
        
    def contracts(self):
        return self._contracts
    
    def authors(self):
        return self._authors 


class Contract:
    
    all = []
    def __init__(self, author = None, book = None, date = None, royalties = None):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        # self.contracts_by_date(date)
        Contract.all.append(self)
        
        if author:
            author._contracts.append(self)
            
        if book:
            author._books.append(self.book)
            book._contracts.append(self)
            book._authors.append(self.author)
            
        if royalties:
            author._royalties += royalties
        
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if isinstance(value, Book):
            self._book = value
        else:
            raise Exception
    
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if type(value) == str:
            self._date = value
        else:
            raise Exception
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if type(value) == int:
            self._royalties = value
        else:
            raise Exception
        
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
        