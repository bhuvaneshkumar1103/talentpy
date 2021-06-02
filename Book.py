'''
create a class Book which has one construcor and 
two functions namely order_book and add_quantity.
'''
class Book:
    # this constructor takes the arguments and assign it to this class variables.
    def __init__(self,name_of_book, author, year_of_publish, price_of_book, no_of_copies_available):
        self.Book_name = name_of_book
        self.Author = author
        self.PublishYear = year_of_publish
        self.Price = price_of_book
        self.Copies = no_of_copies_available
        
    #This method should return price of purchase, if no of books is less than or equal to no_of_copies_available. Else, return “No stock”.
    def order_book(self,no_of_books):
        if no_of_books>self.Copies:
            return "No stock"
        else:
            self.Copies -= no_of_books
            return no_of_books*self.Price
    
    '''
    This method should add quantity of books (2nd param) to existing no_of_copies_available if is_admin is True and return “Book
    quantity updated as <<count>>” . If is_admin is False, return “Unauthorised” as output. 
    '''
    def add_quantity(self,is_admin,quantity):
        if is_admin == True:
            self.Copies +=quantity
            return 'Book quantity updated as ',self.Copies
        else:
            return 'Unauthorized'
book = Book( "Software Quality Assurance", "Mr.Jochen", 1994, 100, 50)
print(book.order_book(10))
print(book.order_book(1000))
print(book.order_book(1))
print(book.order_book(43))
print(book.add_quantity(False, 100))
print(book.add_quantity(True, 2))

'''
Output:
    1000 -> Price of 10 books each book has rs.100
    No stock -> There is no available of the book has been requested.
    100 ->Price of 1 book .
    No stock -> There is no available of the requested Copies.
    Unauthorized ->The authorization for updating is not valid.
    ('Book quantity updated as ', 41) -> Now the no of copies of the book is updated.
'''