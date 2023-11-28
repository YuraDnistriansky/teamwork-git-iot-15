"""
creating a class 'Book' with book parameters 
creating a class 'BookShop' where adds class obgects 'Book'
In class 'BookShop' is sorting class objects 'Book' by parametrs
"""
class Book:
    """
    Class 'Book', that has characteristics of a book in a bookshop
    """
    def __init__(self, attributes):
        """
        passing values to attributes
        """
        self.__name = attributes.get('name')
        self.__price = attributes.get('price')
        self.__number_of_pages = attributes.get('number_of_pages')
        self.__author = attributes.get('author')
        self.__quantity = attributes.get('quantity')
        self.__number_of_sales = attributes.get('number_of_sales')
    @property
    def name(self):
        """
        print name
        """
        return self.__name
    @name.setter
    def name(self, new_name):
        """
        passing new values to name
        """
        self.__name = new_name
    @name.deleter
    def name(self):
        """
        deleting an name
        """
        del self.__name
    @property
    def price(self):
        """
        print price
        """
        return self.__price
    @price.setter
    def price(self, new_price):
        """
        passing new values to price
        """
        self.__price = new_price
    @price.deleter
    def price(self):
        """
        deleting an price
        """
        del self.__price
    @property
    def number_of_pages(self):
        """
        print number 0f pages
        """
        return self.__number_of_pages
    @number_of_pages.setter
    def number_of_pages(self, new_number_of_pages):
        """
        passing new values to number of pages
        """
        self.__number_of_pages = new_number_of_pages
    @number_of_pages.deleter
    def number_of_pages(self):
        """
        deleting an number of pages
        """
        del self.__number_of_pages
    @property
    def author(self):
        """
        print author
        """
        return self.__author
    @author.setter
    def author(self, new_author):
        """
        passing new values to author
        """
        self.__author = new_author
    @author.deleter
    def author(self):
        """
        deleting an author
        """
        del self.__author
    @property
    def quantity(self):
        """
        print quantity
        """
        return self.__quantity
    @quantity.setter
    def quantity(self, new_quantity):
        """
        passing new values to quantity
        """
        self.__quantity = new_quantity
    @quantity.deleter
    def quantity(self):
        """
        deleting an quantity
        """
        del self.__quantity
    @property
    def number_of_sales(self):
        """
        print number of sales
        """
        return self.__number_of_sales
    @number_of_sales.setter
    def number_of_sales(self, new_number_of_sales):
        """
        passing new values to number of sales
        """
        self.__number_of_sales = new_number_of_sales
    @number_of_sales.deleter
    def number_of_sales(self):
        """
        deleting an number of sales
        """
        del self.__number_of_sales
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
    def __del__(self):
        """
        returns a string before deleting the object
        """
        print(f"You deleted the object, that had element {self.__name}")
class BookShop:
    """
    Class, that has the list of books to sort
    can add and remove books
    """
    def __init__(self):
        """
        attributes creation
        """
        self.__books = []
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
    def __del__(self):
        """
        returns a strings befor deleting the object
        """
        print("You deleted the object, that was created based on a class BookShop")
if __name__ == "__main__":
    book_1_data = {
        'name': "Atomic Habits",
        'price': 250,
        'number_of_pages': 200,
        'author': "James Clear",
        'quantity': 30,
        'number_of_sales': 115
    }
    book_1 = Book(attributes=book_1_data)
    book_2_data = {
        'name': "My life and work",
        'price': 320,
        'number_of_pages': 450,
        'author': "Henry Ford",
        'quantity': 50,
        'number_of_sales': 80
    }
    book_2 = Book(attributes=book_2_data)
    book_3_data = {
        'name': "The richest man in Babylon",
        'price': 150,
        'number_of_pages': 180,
        'author': "George Clasyson",
        'quantity': 85,
        'number_of_sales': 150
    }
    book_3 = Book(attributes=book_3_data)
    book_4_data = {
        'name': "Influence",
        'price': 350,
        'number_of_pages': 520,
        'author': "Robert Cialdini",
        'quantity': 25,
        'number_of_sales': 50
    }
    book_4 = Book(attributes=book_4_data)
    book_shop = BookShop()
    book_shop.add_book(book_1)
    book_shop.add_book(book_2)
    book_shop.add_book(book_3)
    book_shop.add_book(book_4)
    print("_" * 20)
    top_books_by_price = book_shop.get_top_books_by_price(4)
    top_books_by_sales = book_shop.get_top_books_by_sales(4)
    print("Top book by price")
    for i, book in enumerate(top_books_by_price, 1):
        print(i, book)
    print("_" * 20)
    print("Top books by sales")
    for i, book in enumerate(top_books_by_sales, 1):
        print(i, book)
    print("_" * 20)
    book_shop.remove_book(book_1)
    book_shop.remove_book(book_2)
    book_shop.remove_book(book_3)
    book_shop.remove_book(book_4)
    