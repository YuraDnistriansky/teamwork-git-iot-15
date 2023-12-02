"""
creating a class 'Book' with book parameters 
creating a class 'BookShop' where adds class obgects 'Book'
In class 'BookShop' is sorting class objects 'Book' by parametrs
"""
import time as t

def line():
    """
    function is going line
    """
    a = 0
    while a < 40:
        print('_', end='')
        t.sleep(0.001)
        a += 1
        
class Book:
    """
    Class 'Book', that has characteristics of a book in a bookshop
    """
    
    def __init__(self, name, price, number_of_pages, author, quantity, number_of_sales):
        """
        passing values to attributes
        """
        self.__name = name
        self.__price = price
        self.__number_of_pages = number_of_pages
        self.__author = author
        self.__quantity = quantity
        self.__number_of_sales = number_of_sales

    @property
    def price(self):
        """
        Returns the price value
        """
        return self.__price
        
    @property
    def number_of_sales(self):
        """
        Returns the number_of_sales value
        """
        return self.__number_of_sales 

    def __str__(self):
        """
        returns a string representation of the object
        """
        return f"{self.__name} by {self.__author} -- Price = {self.__price}" \
               f" -- Sales = {self.__number_of_sales}"
        
    def __repr__(self):
        """
        returns representation of the object, that can be used to restore the object
        """
        return f"Book({self.__name}, {self.__price}, {self.__number_of_pages}," \
               f" {self.__author}, {self.__quantity}, {self.__number_of_sales})"

class BookShop:
    """
    Class, that has the list of books to sort
    can add and remove books
    """
    def __init__(self, books=None):
        """
        attributes creation
        """
        if books is None:
            self.__books = []
        else:
            self.__books = books
            
    def add_book(self, book_add):
        """
        function to add an object to a list that is a attribute of a class
        """
        self.__books.append(book_add)
        
    def remove_book(self, book_remove):
        """
        function to remove an object from a list that is an attribute of a class
        """
        self.__books.remove(book_remove)
        
    def get_top_books_by_price(self, n):
        """
        function to sort by price objects, that are list items
        """
        sorted_books = sorted(self.__books, key=lambda x: x.price, reverse=True)
        return sorted_books[:n]
        
    def get_top_books_by_sales(self, n):
        """
        function to sort by number of sales object, that are list items
        """
        sorted_books = sorted(self.__books, key=lambda x: x.number_of_sales, reverse=True)
        return sorted_books[:n]
        
    def __str__(self):
        """
        returns a string representstion of the oblect
        """
        return "\n".join(str(book) for book in self.__books)
        
    def __repr__(self):
        """
        returns representation of the object, that can be used to restore the object
        """
        return f"BookShop ({self.__books})"
        
if __name__ == "__main__":
    
    book_1 = Book("Atomic Habits", 250, 200, "James Clear", 30, 115)
    book_2 = Book("My life and work", 320, 450, "Henry Ford", 50, 80)
    book_3 = Book("The richest man in Babylon", 150, 180, "George Clasyson", 85, 150)
    book_4 = Book("Influence", 350, 520, "Robert Cialdini", 25, 50)

    book_shop = BookShop()
    book_shop.add_book(book_1)
    book_shop.add_book(book_2)
    book_shop.add_book(book_3)
    book_shop.add_book(book_4)
    
    line()
    
    top_books_by_price = book_shop.get_top_books_by_price(4)
    top_books_by_sales = book_shop.get_top_books_by_sales(4)
    
    print("Top book by price")
    for i, book in enumerate(top_books_by_price, 1):
        print(i, book)
        
    line()
    
    print("Top books by sales")
    for i, book in enumerate(top_books_by_sales, 1):
        print(i, book)

    
