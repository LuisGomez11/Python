
import pickle
from io import open


class Books:
    
    def __init__(self, bookID, bookTitle, author, ISBN, publishYear, category):
        self.bookID = bookID
        self.bookTitle = bookTitle
        self.author = author
        self.ISBN = ISBN
        self.publishYear = publishYear
        self.category = category

    def getBookID(self):
        return self.bookID

    def getBookTitle(self):
        return self.bookTitle

    def getAuthor(self):
        return self.author

    def getISBN(self):
        return self.ISBN

    def getPublishYear(self):
        return self.publishYear

    def getCategory(self):
        return self.category

    def setBookID(self, newID):
        self.bookID = newID

    def setBookTitle(self, newTitle):
        self.bookTitle = newTitle

    def setAuthor(self, newAuthor):
        self.author = newAuthor

    def setISBN(self, newISBN):
        self.ISBN = newISBN

    def setPublishYear(self, newPublishYear):
        self.publishYear = newPublishYear

    def setCategory(self, newCategory):
        self.category = newCategory

    def toString(self):
        print("ID:",self.bookID,"\nTitle:",self.bookTitle,
                "\nAuthor:",self.author,"\nISBN:",self.ISBN,"\nPublish Year:",self.publishYear,
                "\nCategory:",self.category,"\n")

book1 = Books('123','The Legend','Luis Gomez','456123','2019','Action')
book2 = Books('456','Avengers','Diana','68564','2014','Action')
book3 = Books('789','Java','Patricia','436346','2018','Programming')

books = [book1,book2,book3]

fichero = open("Books","wb")

pickle.dump(books,fichero)

fichero.close()

del (fichero)

ficheroApertura = open("Books","rb")

books = pickle.load(ficheroApertura)

ficheroApertura.close()

for b in books:
    b.toString()